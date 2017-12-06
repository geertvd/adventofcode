from sys import argv

script, filename = argv

txt = open(filename)

directions = {
  ">": [1, 0],
  "<": [-1, 0],
  "^": [0, 1],
  "v": [0, -1]
}

santa = {"x":0, "y":0}
robo = {"x":0, "y":0}

houses = {0:{0:1}}
houses_count = 1

i = 0

for char in txt.read():
  step = directions.get(char)
  
  if (i%2):
    carrier = robo
  else: 
    carrier = santa

  carrier["x"] += step[0] 
  carrier["y"] += step[1]

  if carrier.get("x") not in houses:
    houses[carrier.get("x")] = {}
  if carrier.get("y") not in houses[carrier.get("x")]:
    houses[carrier.get("x")][carrier.get("y")] = 1
    houses_count += 1
  
  i += 1

print houses_count
   
	
