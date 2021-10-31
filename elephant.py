#https://codeforces.com/contest/617/problem/A

friend = int(input())
elephant = 0
sol = 0

while elephant < friend:

    if friend-elephant >= 5:
        elephant += 5
    elif friend-elephant >= 4:
        elephant +=4
    elif friend-elephant >= 3:
        elephant += 3
    elif friend-elephant >= 2:
        elephant += 2
    else:
        elephant += 1

    sol += 1

print(sol)
