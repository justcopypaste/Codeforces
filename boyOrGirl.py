#https://codeforces.com/contest/236/problem/A

name = input()

dups = 0
duplicates = []

for letter in name:
    if letter in duplicates:
        dups += 1
    else:
        duplicates.append(letter)

if (len(name) - dups) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
