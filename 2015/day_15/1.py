import re, itertools
input = file('input.txt')

scoreregex = re.compile(r'(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

ingredients = {}
for line in input:
    ingredient, cap, dur, flav, texture, cal = scoreregex.findall(line)[0]
    ingredients[ingredient] = {
        'cap': int(cap),
        'dur': int(dur),
        'flav': int(flav),
        'texture': int(texture)
    }

def sum_to_100(numbers, count):
    combos = []
    for combo in itertools.combinations(numbers, count):
        if sum(combo) == 100:
            combos.append(combo)
    return combos

def calculate_points(ingredients):
    cap = dur = flav = texture = 0
    for ingredient_name in ingredients:
        ingredient = ingredients[ingredient_name]
        cap += ingredient['cap'] * ingredient['tsp']
        dur += ingredient['dur'] * ingredient['tsp']
        flav += ingredient['flav'] * ingredient['tsp']
        texture += ingredient['texture'] * ingredient['tsp']
    return max(cap, 0) * max(dur, 0) * max(flav, 0) * max(texture, 0)

ratios = sum_to_100(range(1,100), len(ingredients))
maxpoints = 0
for permutation in itertools.permutations(ingredients):
    for ratio in ratios:
        recipe = {}
        for i, ingredient in enumerate(permutation):
            recipe[ingredient] = ingredients[ingredient]
            recipe[ingredient]['tsp'] = ratio[i]
        maxpoints = max(calculate_points(recipe), maxpoints)
print maxpoints