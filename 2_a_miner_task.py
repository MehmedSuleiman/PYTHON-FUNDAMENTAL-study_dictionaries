#You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
#Print the resources and their quantities in the following format:
#"{resource} -> {quantity}"
#The quantities will be in the range [1 … 2 000 000 000].
#

dic = {}

while True:
    resource = input()
    if resource == "stop":
        break
    else:
        amount = int(input())
        if resource in dic:
            dic[resource] += amount
        else:
            dic[resource] = amount

for res, amt in dic.items():
    print(f"{res} -> {amt}")