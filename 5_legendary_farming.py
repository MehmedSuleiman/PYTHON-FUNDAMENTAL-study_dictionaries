#You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
#•	"Shadowmourne" - requires 250 Shards
#•	"Valanyr" - requires 250 Fragments
#•	"Dragonwrath" - requires 250 Motes
#"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
#You will be given lines of input in the format:
#"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
#Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
#In the end, print the remaining shards, fragments, and motes in the format:
#"shards: {number_of_shards}
#fragments: {number_of_fragments}
#motes: {number_of_motes}"
#Finally, print the collected junk items in the order of appearance.


materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_obtained = False

while not legendary_obtained:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()

        if material in materials:
            materials[material] += quantity
            if materials[material] >= 250:
                legendary_obtained = True
                materials[material] -= 250
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

# Print key materials
for key in ["shards", "fragments", "motes"]:
    print(f"{key}: {materials[key]}")

# Print junk materials
for key, value in junk.items():
    print(f"{key}: {value}")