#https://codeforces.com/contest/231/problem/A

problems = int(input())
toSolve = 0
for n in range(problems):
    z=0
    inp = input()
    p = int(inp[0])
    v = int(inp[2])
    t = int(inp[-1])
    if p > 0:
        z+=1
    if v > 0:
        z+=1
    if t > 0:
        z+=1

    if z > 1:
        toSolve+=1
print(toSolve)
