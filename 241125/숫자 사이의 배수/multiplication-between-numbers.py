a, b = map(int, input().split())
result = 0
cnt = 0

for i in range(a, b+1):
    if (i % 5 == 0 or i % 7 == 0):
        result += i
        cnt += 1

print("%d %.1f" %(result, round(result/cnt, 1)))