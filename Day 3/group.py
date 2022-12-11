# Author: Rigoberto Mejia
# GitHub username: rmejia4209
# Date: 12/06/2022

# alphabet in lower case followed by upper case
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# this list will contain each letter in the alphabet (lower and upper case)
# the index + 1 will be priority of each unique letter & case
priority_list = []

for letter in alpha:
    priority_list.append(letter)


# um = my_list.index('b')
# print(num)

groups = []
total_priority = 0

with open("rucksack_items.txt", "r") as rucksacks:
    i = 1  # counter to cycle from 0, 1, and 2.
    group = []
    for rucksack in rucksacks:
        rucksack = rucksack.replace("\n", "")
        group.append(rucksack)
        if i % 3 == 0:
            groups.append(group)
            group = []
        i += 1

for group in groups:
    badge = set(group[0]) & set(group[1]) & set(group[2])
    total_priority += priority_list.index(badge.pop()) + 1

print("The total priority is", total_priority)




