n = int(input())
check = list(map(int, input().split()))

check_list = [0] * 24

for i in check:
    check_list[i] += 1
    
for j in range(1, 24):
    print(check_list[j], end = ' ')
