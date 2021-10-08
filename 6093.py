n = int(input())
check = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(check[i], end = ' ')
