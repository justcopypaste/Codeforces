#https://codeforces.com/contest/50/problem/A

inp = input()
row, col = (int(x) for x in inp.split())
domino = row * col * 0.5
print (domino)
