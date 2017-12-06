import random
import copy


def get_move(move_name):
    move = {'cost': 0, 'life': 0, 'damage_effect': [], 'mana_effect': [], 'armor_effect': [], 'damage': 0}
    moves = {
        'magic_missile': {'cost': 53, 'damage': 4},
        'drain': {'cost': 73, 'damage': 2, 'life': 2},
        'shield': {'cost': 113, 'armor_effect': [7] * 6},
        'poison': {'cost': 173, 'damage_effect': [3] * 6},
        'recharge': {'cost': 229, 'mana_effect': [101] * 5}
    }
    move.update(moves[move_name])
    return move


def perform_effects(me, boss):
    me['armor'] = 0
    if me['damage_effect']:
        boss['life'] -= me['damage_effect'][0]
        me['damage_effect'].pop(0)
    if me['mana_effect']:
        me['mana'] += me['mana_effect'][0]
        me['mana_effect'].pop(0)
    if me['armor_effect']:
        me['armor'] = me['armor_effect'][0]
        me['armor_effect'].pop(0)


def attack(move, me, boss):
    perform_effects(me, boss)

    if boss['life'] <= 0:
        return 0

    # execute the new move.
    boss['life'] -= move['damage']
    me['damage_effect'] = move['damage_effect'] if move['damage_effect'] else me['damage_effect']
    me['mana_effect'] = move['mana_effect'] if move['mana_effect'] else me['mana_effect']
    me['armor_effect'] = move['armor_effect'] if move['armor_effect'] else me['armor_effect']
    me['mana'] -= move['cost']
    me['life'] += move['life']

    return move['cost']


def move_is_valid(move, me):
    if move['cost'] > me['mana']:
        return False
    if len(me['damage_effect']) > 1 and move['damage_effect']:
        return False
    if len(me['armor_effect']) > 1 and move['armor_effect']:
        return False
    if len(me['mana_effect']) > 1 and move['mana_effect']:
        return False
    return True


def defend(me, boss):
    perform_effects(me, boss)
    if me['life'] <= 0:
        return
    me['life'] -= max(boss['damage'] - me['armor'], 1)


def fight(me, boss):
    move_names = ['magic_missile', 'drain', 'shield', 'poison', 'recharge']
    rnd = 0
    mana_cost = 0
    while boss['life'] > 0 and me['life'] > 0 and me['mana'] > 53:
        rnd += 1
        if rnd % 2:
            move = get_move(random.choice(move_names))
            while True:
                if move_is_valid(move, me):
                    break
                else:
                    move = get_move(random.choice(move_names))
            mana_cost += attack(move, me, boss)
        else:
            defend(me, boss)

    if boss['life'] <= 0:
        print 'Player wins and spend %d mana!' % mana_cost
        return mana_cost
    else:
        return 0


ME = {'mana': 500, 'life': 50, 'damage': 0, 'armor_effect': [], 'damage_effect': [], 'mana_effect': []}
BOSS = {'life': 71, 'damage': 10}

min_mana = 1000000
for i in xrange(1, 1000000):
    result = fight(copy.deepcopy(ME), copy.deepcopy(BOSS))
    if result:
        min_mana = min(min_mana, result)

print 'Least mana spend: %d' % min_mana
