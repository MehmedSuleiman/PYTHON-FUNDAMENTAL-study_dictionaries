#Write a program that counts all characters in a string except for space (" ").
#Print all the occurrences in the following format:
#"{char} -> {occurrences}"

char = list(input().split(" "))

chars = {}
for word in char:
    for letter in word:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1


for i in chars :
    print(f"{i} -> {chars[i]}")