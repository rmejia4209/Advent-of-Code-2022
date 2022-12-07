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
# X - Lose (0 pt)
# Y - Tie (3 pt)
# Z - Win (6 pt)

# Scoring guide
# 1 pt for rock
# 2 pt for paper
# 3 pt for scissor

points_dict = {"A X": 3,
               "A Y": 4,
               "A Z": 8,
               "B X": 1,
               "B Y": 5,
               "B Z": 9,
               "C X": 2,
               "C Y": 6,
               "C Z": 7}

total_points = 0

with open("rps_strategy.txt", "r") as file_object:
    for line in file_object:
        line = line.replace("\n", "")
        total_points += points_dict[line]

print(total_points)