#https://codeforces.com/contest/112/problem/A

first = input().lower()
sec = input().lower()

if first > sec:
    print('1')
if sec > first:
    print('-1')
if first == sec:
    print('0')
