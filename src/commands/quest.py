from datetime import timedelta
import random

from command import *
from consume import *
from data import terms, definitions
from polling import *
from util import *

_quests = load_state("Quests")


def _quest_timer(time, args):
    quest, thread_id = args["Quest"], args["ThreadID"]
    if thread_id not in _quests:
        add_passive_consumption(None, thread_id, "Quest")
    _quests[thread_id] = quest
    client.send(Message(quest["Question"]), thread_id, ThreadType.GROUP)
    save_state("Quests", _quests)


def _quest_handler(author, text, thread_id, thread_type):
    try:
        choices = int(text) if len(text) else 5
        choices = min(max(choices, 2), 20)
    except ValueError:
        return False
    indices = random.sample(range(0, len(terms)), choices)
    correct = random.randint(0, choices - 1)
    if random.randint(0, 1):
        quest = {}
        quest["Question"] = "Which word means \"{}\"?".format(definitions[indices[correct]])
        quest["Answers"] = [terms[index] for index in indices]
    else:
        quest = {}
        quest["Question"] = "What does \"{}\" mean?".format(terms[indices[correct]])
        quest["Answers"] = [definitions[index] for index in indices]
    for i, answer in enumerate(quest["Answers"]):
        quest["Question"] += "\n{}. {}".format(i + 1, answer)
    quest["Correct"] = correct
    quest["Attempted"] = []

    if thread_type == ThreadType.USER:
        if thread_id not in _quests:
            add_active_consumption(None, thread_id, ThreadType.USER, "Quest", quest["Question"])
        _quests[thread_id] = quest
        save_state("Quests", _quests)
    else:
        add_timer(datetime.now() + timedelta(seconds=3), _quest_timer, {"Quest": quest, "ThreadID": thread_id})
        client.send(Message("A quest will be sent out in 3 seconds."), thread_id, thread_type)
    return True


def _prompt_handler(author, text, thread_id, thread_type, args):
    if thread_id not in _quests:
        return True
    quest = _quests[thread_id]
    try:
        text = int(text)
        assert 0 < text <= len(quest["Answers"])
    except (AssertionError, TypeError, ValueError):
        if thread_type == ThreadType.USER:
            client.send(Message("Not a valid answer."), thread_id, thread_type)
        return False

    if author["_id"] not in quest["Attempted"]:
        quest["Attempted"].append(author["_id"])
        if text == quest["Correct"] + 1:
            del _quests[thread_id]
            reward = int(len(quest["Answers"]) * random.uniform(2, 10))
            author["Gold"] += reward
            user_update(author["_id"], {"$set": {"Gold": author["Gold"]}})
            reply = "{} has gained {} gold ".format(author["Name"], format_num(reward, truncate=True))
            reply += "and is now at {} gold total!".format(format_num(author["Gold"] + reward, truncate=True))
            client.reactToMessage(client.last_message.uid, MessageReaction.YES)
            client.send(Message(reply), thread_id, thread_type)
            save_state("Quests", _quests)
            return True
        else:
            client.reactToMessage(client.last_message.uid, MessageReaction.NO)
            # - If this is a user thread, remove the active consumer to prevent blocking
            if thread_type == ThreadType.USER and author["_id"] == thread_id:
                del _quests[thread_id]
                save_state("Quests", _quests)
                return True
    return False


_quest_info = """<<Quest>>
*Usage*: "!quest"
Generates a multiple choice question. The first correct response will reward gold. Only one response per user.

*Usage*: "!quest <choices>"
*Example*: "!quest 8"
Generates a multiple choice question with <choices> choices. Can be between 2 and 20.
"""

map_user_command(["quest", "q"], _quest_handler, 2, _quest_info)
map_group_command(["quest", "q"], _quest_handler, 0, _quest_info)
add_handler("Quest", _prompt_handler)
