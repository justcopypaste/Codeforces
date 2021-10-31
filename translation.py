#https://codeforces.com/contest/41/problem/A

word = input()
reverse = word[::-1]

trans = input()

if trans == reverse:
    print("YES")
else:
    print("NO")
