#https://codeforces.com/contest/110/problem/A

number = input()
luckies = 0
for num in number:
    if int(num) == 4 or int(num) == 7:
        luckies += 1
if(luckies == 4 or luckies == 7):
    print("YES")
else:
    print("NO")
