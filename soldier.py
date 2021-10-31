#https://codeforces.com/contest/546/problem/A

k,n,w = map(int, input().split())
sol = 0
for i in range(w):
    sol += (i+1)*k

if sol - n > 0:
    print(sol - n)
else:
    print(0)
