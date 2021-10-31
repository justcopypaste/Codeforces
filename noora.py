#https://codeforces.com/contest/810/problem/A

firstIn = input()
n, k = (int(x) for x in firstIn.split())

secIn = input()
grades = [float(x) for x in secIn.split()]

suma = 0
steps = 0

for i in range(n):
    suma = suma + grades[i]

while (suma/n) < (k - 0.5):
    suma = suma + k
    n += 1
    steps+=1

print(steps)
