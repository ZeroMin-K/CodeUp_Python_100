n = int(input())

sum = 0
for i in range(n+1):
    if sum >= n:
        print(i-1)
        break
    sum += i
