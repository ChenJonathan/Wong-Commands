import math

priority_names = ['Peasant', 'User', 'Mod', 'Admin', 'Master']

master_priority = len(priority_names) - 1
master_id = '1564703352'


def base_stat_float(level):
    return (math.sqrt(level + 64) - 7) * 10


def base_stat(level):
    return int(base_stat_float(level))


def equip_atk(user):
    return user['Equipment']['Weapon']['ATK'] + \
           user['Equipment']['Armor']['ATK'] + \
           user['Equipment']['Accessory']['ATK']


def equip_def(user):
    return user['Equipment']['Weapon']['DEF'] + \
           user['Equipment']['Armor']['DEF'] + \
           user['Equipment']['Accessory']['DEF']


def equip_spd(user):
    return user['Equipment']['Weapon']['SPD'] + \
           user['Equipment']['Armor']['SPD'] + \
           user['Equipment']['Accessory']['SPD']


def total_atk(user):
    return base_stat(user['Stats']['Level']) + equip_atk(user)


def total_def(user):
    return base_stat(user['Stats']['Level']) + equip_def(user)


def total_spd(user):
    return base_stat(user['Stats']['Level']) + equip_spd(user)


def format_num(num, sign=False, truncate=False):
    suffixes = ['', 'k', 'm', 'b', 't']
    scale = 0
    if truncate:
        while abs(num) >= 100000 and scale < len(suffixes) - 1:
            num = num // 1000
            scale += 1
    num = ('+' + str(num)) if sign and num >= 0 else str(num)
    return num + suffixes[scale]


def calculate_score(user):
    score = math.pow(max(user['Gold'] + user['GoldFlow'] * 50, 0), 0.25) * 50
    score += (total_atk(user) + total_def(user) + total_spd(user) - 45) * 25
    for location, progress in user['LocationProgress'].items():
        if progress == 1:
            score += 50
    score -= 16 * 50
    return int(score)