from itertools import combinations

input = __import__('sys').stdin.readline
N = int(input())

dec = set()

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        dec.add(int(num))

dec = sorted(dec)

if N >= len(dec): print(-1)
else: print(dec[N])