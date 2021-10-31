#https://codeforces.com/contest/977/problem/A

num, times = map(int, input().split())

for i in range(times):
    if num % 10 == 0 :
        num = num / 10

    else:
        num -= 1

print(int(num))
