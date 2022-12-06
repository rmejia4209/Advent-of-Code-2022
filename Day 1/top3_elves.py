# Author: Rigoberto Mejia
# GitHub username: rmejia4209
# Date: 12/05/2022
# Description: This program determines the total calorie count of the top 3 elves


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

print(elf_calories)
elf_calories.sort(reverse=True)
print(elf_calories)
calories_of_top_3 = 0

for i in range(0,3):
    print("adding", str(elf_calories[i]))
    calories_of_top_3 += elf_calories[i]

print("The top three elves have", str(calories_of_top_3), "calories amongst themselves.")