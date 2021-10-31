#https://codeforces.com/contest/271/problem/A

num = int(input()) + 1
ans = False

while not ans:
    digits = []
    for n in str(num):
        digits.append(int(n))

    ans = len(set(digits)) == len(digits)
    if not ans:
        num += 1

print(num)
