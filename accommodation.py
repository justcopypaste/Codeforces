#https://codeforces.com/contest/467/problem/A

rooms = 0

for i in range(int(input())):
    p, q = map(int, input().split())

    if(q >= p+2):
        rooms += 1

print(rooms)
