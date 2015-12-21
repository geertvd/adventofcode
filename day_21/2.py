from __future__ import division
import re
import itertools
import math


def get_armory_group(shop_category):
    shop_category = shop_category.strip()
    re_split = re.compile(r'(.+)\s*\s(\d+)\s*(\d+)\s*(\d+)')
    items = []
    for shop_item in shop_category.split('\n')[1:]:
        name, cost, damage, armor = re_split.findall(shop_item)[0]
        items.append({
            'name': name.strip(),
            'cost': int(cost),
            'damage': int(damage),
            'armor': int(armor)
        })
    return items


def win_fight(me, boss):
    me['hit'] = max(me['damage'] - boss['armor'], 1)
    boss['hit'] = max(boss['damage'] - me['armor'], 1)
    return math.ceil(me['hit points'] / boss['hit']) >= math.ceil(boss['hit points'] / me['hit'])


def get_stats(weapon, armor=False, rings=[]):
    me = dict()
    me['hit points'] = 100
    me['damage'] = weapon['damage'] + sum(map(lambda x: x['damage'], rings))
    me['armor'] = 0
    me['cost'] = weapon['cost'] + sum(map(lambda x: x['cost'], rings))
    if armor:
        me['armor'] += armor['armor']
        me['cost'] += armor['cost']
    me['armor'] += sum(map(lambda x: x['armor'], rings))
    return me


shop_categories = file('shop.txt').read().split('\n\n')
weapons = get_armory_group(shop_categories[0])
armory = get_armory_group(shop_categories[1])
armory.append({'name': 'dummy armor', 'cost': 0, 'damage': 0, 'armor': 0})
rings = get_armory_group(shop_categories[2])
rings.append({'name': 'dummy ring', 'cost': 0, 'damage': 0, 'armor': 0})
rings.append({'name': 'dummy ring 2', 'cost': 0, 'damage': 0, 'armor': 0})
ring_combos = list(itertools.combinations(rings, 2))


boss = {}
for line in file('boss.txt'):
    name, points = line.split(': ')
    boss[name.lower()] = int(points)

max_cost = 0
for weapon in weapons:
    for armor in armory:
        for ring_combo in ring_combos:
            me = get_stats(weapon, armor, ring_combo)
            if not win_fight(me, boss):
                max_cost = max(me['cost'], max_cost)

print max_cost

