result = 0
cnt = 0

for _ in range(10):
    n = int(input())

    if 200 >= n >= 0:
        result += n
        cnt += 1

average = round(result / cnt, 1)

print(result, average, sep=" ")