#https://codeforces.com/contest/158/problem/A

inp = input()
part, win = (int(x) for x in inp.split())
winners = 0
lastScore = 0
scores = input()

for strscore in scores.split():
    score = int(strscore)
    if score > 0:
        if winners < win:
            winners+=1
            lastScore = score
        else:
             if score >= lastScore:
                 winners+=1

print(winners)
