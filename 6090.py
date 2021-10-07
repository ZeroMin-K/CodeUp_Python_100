a, m, d, n = map(int, input().split())

seq = a
for _ in range(1, n):
    seq = m * seq + d

print(seq)
