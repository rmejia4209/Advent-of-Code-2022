# Author: Rigoberto Mejia
# GitHub username: rmejia4209
# Date: 12/06/2022

num_matches = 0

with open("pairs.txt", "r") as pairs:
    for pair in pairs:
        pair = pair.replace("\n", "")
        pair = pair.split(",")
        pair_one = list(range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1))
        pair_two = list(range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1))

        if all(item in pair_one for item in pair_two) or all(item in pair_two for item in pair_one):
            print(pair_one)
            print(pair_two)
            num_matches += 1

print("Matches:", num_matches)
