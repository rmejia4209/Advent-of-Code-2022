# Author: Rigoberto Mejia
# GitHub username: rmejia4209
# Date: 12/06/2022
# Description: This program determines the final score if the proposed strategy is followed

# Key
# Opponent
# A - Rock
# B - Paper
# C - Scissors
# Player
# X - Rock (1 pt)
# Y - Paper (2 pt)
# Z - Scissors (3 pt)

# Scoring guide
# 0 pt for lose
# 3 pt for tie
# 6 pt for win

points_dict = {"A X": 4,
               "A Y": 8,
               "A Z": 3,
               "B X": 1,
               "B Y": 5,
               "B Z": 9,
               "C X": 7,
               "C Y": 2,
               "C Z": 6}

total_points = 0

with open("rps_strategy.txt","r") as file_object:
    for line in file_object:
        line = line.replace("\n", "")
        total_points += points_dict[line]
        
print(total_points)
