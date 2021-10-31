#https://codeforces.com/contest/339/problem/B

fistIn = input()
n, m = (int(x) for x in fistIn.split())

secIn = input()
houses = [int(x) for x in secIn.split()]

xania = 1
steps = 0

for x in range(m):
    if xania < houses[x]:
        steps = steps + (houses[x] - xania)
        xania = houses[x]
    elif xania > houses[x]:
        steps = steps + (n - xania + houses[x])
        xania = houses[x]
     
print(steps)
