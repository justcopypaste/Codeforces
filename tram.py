#https://codeforces.com/contest/116/problem/A

n = int(input())

curr = 0
max = 0

for i in range(n):
    Out,In = map(int, input().split())
    curr = curr + In - Out
    if curr > max:
        max = curr

print(max)
