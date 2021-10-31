#https://codeforces.com/contest/266/problem/A

n = int(input())
s = input()

pairs = 0
for i in range(n-1):
    if(s[i] == s[i+1]):
        pairs +=1

print(pairs)
