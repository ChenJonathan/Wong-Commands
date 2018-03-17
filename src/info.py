from fbchat.models import *

from enums import Location
from util import *


def generate_user_info(client, author, command):
    command = command.lower()

    if len(command) == 0:
        reply = '<<Command List>>\n'
        reply += '!alias: Alias assignment\n'
        reply += '!check: See user statistics\n'
        reply += '!define: Command remapping\n'
        reply += '!equip: Change level / stats\n'
        reply += '!explore: Check activity\n'
        reply += '!help: Read documentation\n'
        reply += '!message: Gateway messaging\n'
        reply += '!perm: Change user priority\n'
        reply += '!response: Response priming\n'
        reply += '!secret: List active secrets\n'
        reply += '!warp: Change location\n'
        reply += '(See how commands work with "!help <command>")'
    
    elif command == 'alias':
        reply = '<<Alias>>\n'
        reply += 'Usage: "!alias <alias> <name>"\n'
        reply += 'Example: "!alias wong Wong Liu"\n'
        reply += 'Assigns an alias to a user (found using <name>) for '
        reply += 'use in other private chat commands. Aliases must be a single word.'

    elif command == 'check':
        reply = '<<Check>>\n'
        reply += 'Usage: "!check <type> <name>"\n'
        reply += 'Example: "!check Justin"\n'
        reply += 'Example: "!check equip Justin"\n'
        reply += 'Lists some information on the user designated by <alias> (or all users with aliases, '
        reply += 'if left blank). The type of information is specified by <type> (or "stat", if left blank). '
        reply += 'Current information types include the following:\n'
        reply += '-> "Stat" - Statistics\n'
        reply += '-> "Equip" - Equipment\n'
        reply += '-> "Talent" - Talents\n'

    elif command == 'define':
        reply = '<<Define>>\n'
        reply += 'Usage: "!define <command> <mapping>"\n'
        reply += 'Example: "!define quit !mute"\n'
        reply += 'Example: "!define roll Jonathan Chen rolls a 6."\n'
        reply += 'Remaps <command> so that using it has the effect of the command '
        reply += 'specified in <mapping>. If <mapping> is not a command, Wong will '
        reply += 'instead send <mapping> as a message. Note that these mappings only '
        reply += 'apply to you.\n\n'
        reply += 'Usage: "!define <command>"\n'
        reply += 'Clears the mapping for <command> to its default.'

    elif command == 'equip':
        reply = '<<Equip>>\n'
        reply += 'Usage: "!equip <level> <attack> <defence> <speed>"\n'
        reply += 'Example: "!equip 1 2 2 2"\n'
        reply += 'Sets your level to <level> and equips items with a stat total of '
        reply += '<attack> attack, <defence> defence, and <speed> speed.'

    elif command == 'explore':
        reply = '<<Explore>>\n'
        reply += 'Usage: "!explore"\n'
        reply += 'Shows the number of people that have explored this hour. '
        reply += 'Used as a measure of activity.'

    elif command == 'help':
        reply = '<<Help>>\n'
        reply += 'Usage: "!help"\n'
        reply += 'Lists all the user commands that you can use. Differs per person.\n\n'
        reply += 'Usage: "!help <command>"\n'
        reply += 'Example: "!help secret"\n'
        reply += 'Explains the syntax and effects of the provided user <command>.'

    elif command == 'message':
        reply = '<<Message>>\n'
        reply += 'Usage: "!message <alias> <message>"\n'
        reply += 'Example: "!message raph This is Wong."\n'
        reply += 'Sends a message from Wong to the user designated by <alias>.\n\n'
        reply += 'Usage: "!message <alias>"\n'
        reply += 'Example: "!message raph"\n'
        reply += 'Sends the default chat emoji from Wong to the user designated by <alias>.'

    elif command == 'perm':
        reply = '<<Perm>>\n'
        reply += 'Usage: "!perm <priority> <alias>"\n'
        reply += 'Example: "!perm 0 raph"\n'
        reply += 'Sets the priority of the user designated by <alias> to <priority>.'

    elif command == 'response':
        reply = '<<Response>>\n'
        reply += 'Usage: "!response <response>"\n'
        reply += 'Example: "!response Anime belongs in the trash."\n'
        reply += 'Primes a response for Wong. The next time you talk to Wong, his '
        reply += 'normal response will be replaced by <response>. Multiple responses '
        reply += 'can be primed at once - older responses will be used first.'

    elif command == 'secret':
        reply = '<<Secret>>\n'
        reply += 'Usage: "!secret"\n'
        reply += 'Lists all of your active secrets. This includes command mappings '
        reply += '(!define) and primed responses (!response).'

    elif command == 'warp':
        reply = '<<Warp>>\n'
        reply += 'Usage: "!warp <location>"\n'
        reply += 'Sends you to the location designated by <location> instantly. This '
        reply += 'cancels your current journey if you are traveling somewhere.'

    else:
        reply = 'Not a valid command.'
    client.send(Message(reply), thread_id=author['_id'])


def generate_group_info(client, author, command, thread_id):
    command = command.lower()

    if len(command) == 0:
        reply = '<<Command List>>\n'
        reply += 'See how commands work with "!help <command>".\n'
        if author['_id'] == master_id:
            reply += '\n<Master Commands>\n'
            reply += '!alias: Alias assignment\n'
            reply += '!perm: Change user priority\n'
            reply += '!warp: Change location\n'
        reply += '\n<Game Commands>\n'
        reply += '!battle: Battle monsters\n'
        reply += '!check: See user statistics\n'
        reply += '!craft: Craft items with materials\n'
        reply += '!duel: Duel another player\n'
        reply += '!explore: Gather materials\n'
        reply += '!give: Give someone gold\n'
        reply += '!inventory: Check your inventory\n'
        reply += '!jail: Send someone to jail\n'
        reply += '!map: See your location\n'
        reply += '!quest: Solve quizzes for gold\n'
        reply += '!score: Show group rankings\n'
        reply += '!shop: Spend gold to buy things\n'
        reply += '!talent: Allocate talent points\n'
        reply += '!travel: Travel around the world\n'
        reply += '\n<Miscellaneous Commands>\n'
        reply += '!bully: Harass someone\n'
        reply += '!daily: Subscribe to daily events\n'
        reply += '!help: Read documentation\n'
        reply += '!mute: Remove from group\n'
        reply += '!notes: See recent changes\n'
        reply += '!random: Random emoji / color\n'
        reply += '!roll: Roll the dice'

    elif command == 'alias':
        reply = '<<Alias>>\n'
        reply += 'Usage: "!alias <alias> <name>"\n'
        reply += 'Example: "!alias wong Wong Liu"\n'
        reply += 'Assigns an alias to a user (found using <name>) for '
        reply += 'use in other private chat commands. Aliases must be a single word. '
        reply += 'Only usable by ' + priority_names[master_priority] + ' priority.'

    elif command == 'battle':
        reply = '<<Battle>>\n'
        reply += 'Usage: "!battle"\n'
        reply += 'Generates a random monster for you to fight. The monster\'s strength is based '
        reply += 'on the current location and your level. Defeating monsters will reward you with '
        reply += 'experience and gold. The amount of gold scales up with your gold gain per hour. '
        reply += 'Quest and battle gold rewards scale up with your level. Health is restored fully '
        reply += 'every hour.'

    elif command == 'bully':
        reply = '<<Bully>>\n'
        reply += 'Usage: "!bully <name>"\n'
        reply += 'Example: "!bully Justin"\n'
        reply += 'Generates an insult for a user (found using <name>).'

    elif command == 'check':
        reply = '<<Check>>\n'
        reply += 'Usage: "!check <type> <name>"\n'
        reply += 'Example: "!check Justin"\n'
        reply += 'Example: "!check equip Justin"\n'
        reply += 'Lists some information on the user designated by <name> (or yourself, if left blank). '
        reply += 'The type of information is specified by <type> (or "stat", if left blank). '
        reply += 'Current information types include the following:\n'
        reply += '-> "Stat" - Statistics\n'
        reply += '-> "Equip" - Equipment\n'
        reply += '-> "Talent" - Talents\n'

    elif command == 'craft':
        reply = '<<Craft>>\n'
        reply += 'Usage: "!craft"\n'
        reply += 'Lists all the items available to craft. Different locations will offer '
        reply += 'different crafting recipes.\n\n'
        reply += 'Usage: "!craft <slot>"\n'
        reply += 'Example: "!craft 1"\n'
        reply += 'Crafts the item designated by <slot>. Make sure to check the craft list '
        reply += 'first to see which item is in each slot.'

    elif command == 'daily':
        reply = '<<Daily>>\n'
        reply += 'Usage: "!daily <event>"\n'
        reply += 'Example: "!daily emoji"\n'
        reply += 'Toggles the group\'s subscription to <event>. Events occur at midnight '
        reply += 'EST. Current events include the following:\n'
        reply += '-> "Color" - Changes the chat color\n'
        reply += '-> "Emoji" - Changes the chat emoji'

    elif command == 'duel':
        reply = '<<Duel>>\n'
        reply += 'Usage: "!duel <amount> <name>"\n'
        reply += 'Example: "!duel 100 Justin"\n'
        reply += 'Sends a duel request to the user designated by <name> with a bet of <amount>. '
        reply += 'The bet is refunded if the duel is cancelled. Duel requests can be accepted by '
        reply += 'sending a duel request back with the same <amount>. Only one duel request can '
        reply += 'be active at a time per person.\n\n'
        reply += 'Usage: "!duel cancel"\n'
        reply += 'Cancels your current duel request.'

    elif command == 'explore':
        reply = '<<Explore>>\n'
        reply += 'Usage: "!explore"\n'
        reply += 'Explores the current location. Exploration will grant various rewards '
        reply += 'and gradually discover surrounding locations. Can be done once per hour; '
        reply += 'the explore timer resets on the hour.'

    elif command == 'give':
        reply = '<<Give>>\n'
        reply += 'Usage: "!give <amount> <name>"\n'
        reply += 'Example: "!give 10 Justin"\n'
        reply += 'Gives <amount> gold to the user designated by <name>.'

    elif command == 'help':
        reply = '<<Help>>\n'
        reply += 'Usage: "!help"\n'
        reply += 'Lists all the group commands that you can use.\n\n'
        reply += 'Usage: "!help <command>"\n'
        reply += 'Example: "!help quest"\n'
        reply += 'Explains the syntax and effects of the provided group <command>.'

    elif command == 'inventory':
        reply = '<<Inventory>>\n'
        reply += 'Usage: "!inventory"\n'
        reply += 'Lists the contents of your inventory to you in a private message. '
        reply += 'Items can be found through exploration. There is no limit to '
        reply += 'inventory size.'

    elif command == 'jail':
        reply = '<<Jail>>\n'
        reply += 'Usage: "!jail"\n'
        reply += 'Sends a person to jail, preventing them from taking any actions (such as '
        reply += 'questing or exploring). If the person is already in jail, they will be '
        reply += 'freed from jail instead and sent to ' + Location['Lith Harbor'].name + '. '
        reply += 'Only usable by ' + priority_names[master_priority - 1] + ' priority and above.'

    elif command == 'map':
        reply = '<<Map>>\n'
        reply += 'Usage: "!map>"\n'
        reply += 'Posts a visual of your current region.'

    elif command == 'mute':
        reply = '<<Mute>>\n'
        reply += 'Usage: "!mute <name>"\n'
        reply += 'Example: "!mute Justin"\n'
        reply += 'Kicks a user (found using <name>) from the group chat.'

    elif command == 'notes':
        reply = '<<Notes>>\n'
        reply += 'Usage: "!notes"\n'
        reply += 'Displays information regarding recent updates.'

    elif command == 'perm':
        reply = '<<Perm>>\n'
        reply += 'Usage: "!perm <priority> <name>"\n'
        reply += 'Example: "!perm 0 Justin"\n'
        reply += 'Sets the priority of the user designated by <name> to <priority>. '
        reply += 'Only usable by ' + priority_names[master_priority] + ' priority.'

    elif command == 'quest':
        reply = '<<Quest>>\n'
        reply += 'Usage: "!quest"\n'
        reply += 'Generates a multiple choice question for you. You answer by replying with '
        reply += 'the choice number. Correct responses will reward gold but incorrect ones '
        reply += 'will cost you. The amount of gold scales up with your gold gain per hour.\n\n'
        reply += 'Usage: "!quest <type>"\n'
        reply += 'Example: "!quest psych"\n'
        reply += 'Sets the type of multiple choice question that will be generated '
        reply += 'for you. Current quest types include the following:\n'
        reply += '-> "Vocab" - GRE vocabulary\n'
        reply += '-> "Econ" - Economics\n'
        reply += '-> "Gov" - U.S. government\n'
        reply += '-> "History" - World history\n'
        reply += '-> "Psych" - Psychology\n'
        reply += '-> "Science" - Physics / chemistry / biology\n'
        reply += '-> "Trivia" - Trivia (many topics)'

    elif command == 'random':
        reply = '<<Random>>\n'
        reply += 'Usage: "!random"\n'
        reply += 'Randomly sets the group chat\'s color and emoji.'

    elif command == 'roll':
        reply = '<<Roll>>\n'
        reply += 'Usage: "!roll <sides>"\n'
        reply += 'Example: "!roll 10"\n'
        reply += 'Rolls a <sides> sided die. <sides> defaults to 6 if left blank.'

    elif command == 'score':
        reply = '<<Score>>\n'
        reply += 'Usage: "!score <page>"\n'
        reply += 'Example: "!score 2"\n'
        reply += 'Lists the top people in the group chat by score. Score takes total stats, gold, '
        reply += 'gold generation, and locations discovered into account. Each page lists 9 people.'

    elif command == 'shop':
        reply = '<<Shop>>\n'
        reply += 'Usage: "!shop"\n'
        reply += 'Lists all the items available in the shop. Shop items are the same '
        reply += 'in every location that has a shop.\n\n'
        reply += 'Usage: "!shop <slot> <amount>"\n'
        reply += 'Example: "!shop 1 10"\n'
        reply += 'Purchases <amount> copies of the shop item designated by <slot>. '
        reply += '<amount> defaults to 1 if left blank. Make sure to check "!shop" '
        reply += 'first to see which item is in each slot.'

    elif command == 'talent':
        reply = '<<Talent>>\n'
        reply += 'Usage: "!talent"\n'
        reply += 'Lists information on all available talents.\n\n'
        reply += 'Usage: "!talent <slot> <amount>"\n'
        reply += 'Example: "!talent 2 3"\n'
        reply += 'Allocates <amount> points to the talent designated by <slot>. '
        reply += '<amount> defaults to 1 if left blank. Make sure to check "!talent" '
        reply += 'first to see which talent is in each slot.\n\n'
        reply += 'Usage: "!talent reset"\n'
        reply += 'Resets all talents allocated. This costs 10% of your current gold per hour.'

    elif command == 'travel':
        reply = '<<Travel>>\n'
        reply += 'Usage: "!travel <location>"\n'
        reply += 'Example: "!travel Ellinia"\n'
        reply += 'Sets your character on a journey to <location>. You will be unable to '
        reply += 'take most actions (such as shopping or exploring) while traveling.\n\n'
        reply += 'Usage: "!travel cancel"\n'
        reply += 'Cancels your current journey. You will be returned to your previous location.\n\n'
        reply += 'Usage: "!travel"\n'
        reply += 'Shows your information about your current location as well as which locations you '
        reply += 'can travel to from your current location. New locations can be found through exploration.'

    elif command == 'warp':
        reply = '<<Warp>>\n'
        reply += 'Usage: "!warp <location>"\n'
        reply += 'Sends you to the location designated by <location> instantly. This '
        reply += 'cancels your current journey if you are traveling somewhere. '
        reply += 'Only usable by ' + priority_names[master_priority] + ' priority.'

    else:
        reply = 'Not a valid command.'
    client.send(Message(reply), thread_id=thread_id, thread_type=ThreadType.GROUP)