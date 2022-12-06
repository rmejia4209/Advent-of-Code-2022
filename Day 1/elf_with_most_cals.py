# Author: Rigoberto Mejia
# GitHub username: rmejia4209
# Date: 11/23/2022
# Description: This program determines the elf that has the most amount of calories available


# elf_calories is a list that will hold the total calories carried by each elf
elf_calories = []

with open("calories_by_elf.txt", "r") as file_object:
    calories = 0
    for line in file_object:
        if line != "\n":
            calories += int(line)  # keep summing calories until a new line is encountered
        else:
            elf_calories.append(calories)  # add calories to the list
            calories = 0  # reset calorie counter to 0

king_elf = elf_calories.index(max(elf_calories))  # index of the elf with most amount of calories

print("The elf with the most amount of calories is ", king_elf, ".", sep="")
print("He has", str(elf_calories[king_elf]), "calories on him.")




