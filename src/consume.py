_user_map = {}
_group_map = {}


def try_user_consumption(client, author, text, thread_id):
    author_id = author["_id"]
    if author_id not in _user_map:
        return False

    result = _user_map[author_id][0](client, author, text, thread_id)
    if result:
        _user_map[author_id].pop(0)
        if not len(_user_map[author_id]):
            del _user_map[author_id]
        return True
    return False


def add_user_consumption(user_id, handler):
    if user_id not in _user_map:
        _user_map[user_id] = []
    _user_map[user_id].append(handler)


def try_group_consumption(client, author, text, thread_id):
    author_id = author["_id"]
    if thread_id not in _group_map:
        return False
    current_map = _group_map[thread_id]

    if author_id in current_map:
        current_key = author_id
    elif None in current_map:
        current_key = None
    else:
        return False

    result = current_map[current_key][0](client, author, text, thread_id)
    if result:
        current_map[current_key].pop(0)
        if not len(current_map[current_key]):
            del current_map[current_key]
            if not len(current_map):
                del _group_map[thread_id]
        return True
    return False


def add_group_consumption(user_id, thread_id, handler):
    if thread_id not in _group_map:
        _group_map[thread_id] = {}
    current_map = _group_map[thread_id]
    if user_id not in current_map:
        current_map[user_id] = []
    current_map[user_id].append(handler)