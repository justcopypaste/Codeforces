#https://codeforces.com/contest/734/problem/A

games = int(input())
anton = 0
danik = 0

wins = input()

for win in wins:
    if win == 'A':
        anton += 1
    else:
        danik += 1

if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')
