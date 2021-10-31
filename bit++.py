#https://codeforces.com/contest/282/problem/A

i = int(input())
x = 0
for n in range(i):
    inp = input()
    if inp.find('+') == -1:
        x-=1
    else:
        x+=1
print(x)
