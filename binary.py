cases = int(input())

output = []

for x in range(cases):
    n = int(input())
    bin = int(input())
    binstr = str(bin)
    out = ''

    for i in range(n):
        if(i % 2 == 0):
            out = out + binstr[i]
        else:
            out=out+'0'

    output.append(out)

for o in output:
    print(int(o))
