#https://codeforces.com/contest/339/problem/A

inp = input()
nums = []
for num in inp.split('+'):
    nums.append(int(num))
nums.sort()
solution = ''
for i in nums:
    solution = str(i) if solution == '' else solution + '+' + str(i)

print(solution)
