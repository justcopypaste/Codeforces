#https://codeforces.com/contest/71/problem/A

num = int(input())
words = []
for n in range(num):
    words.append(input())

for n in range(len(words)):
    word = words[n]
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    print(word)
