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

total_priority = 0

with open("rucksack_items.txt", "r") as rucksacks:
    for rucksack_items in rucksacks:
        rucksack_items = rucksack_items.replace("\n", "")  # remove the new line at the end of the string
        rucksack_comp_1 = slice(0, len(rucksack_items)//2)  # slice object for 1st compartment of rucksack
        rucksack_comp_2 = slice(len(rucksack_items)//2, len(rucksack_items))  # slice object for the 2nd compartment

        # for loop to go item by item in 1st compartment & to find a match in the 2nd compartment
        for item in rucksack_items[rucksack_comp_1]:
            if item in rucksack_items[rucksack_comp_2]:
                priority = priority_list.index(item) + 1  # find the priority of the matched item
                total_priority += priority  # add to the total priority
                break  # move on to the next rucksack


print("The total priority is", str(total_priority))
