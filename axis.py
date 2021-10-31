#https://codeforces.com/contest/1401/problem/A

firstIn = int(input())

results = []

for n in range(firstIn):
    inp = input()
    astr, kstr = inp.split()
    a = int(astr)
    k = int(kstr)

    if a < k:
        results.append(k-a)
    elif  (a % 2) == (k % 2):
        results.append(0)
    else:
        results.append(1)

for result in results:
    print(result)
