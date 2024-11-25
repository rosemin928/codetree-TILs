n = int(input())
result = 0

for _ in range(n):
    i = int(input())
    result += i

print(result, round(result / n, 1), sep=" ")