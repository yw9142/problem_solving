""" 기존 풀이
def get_divisor(n):
    result = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            result.append(i)
            if ((i ** 2) != n):
                result.append(n // i)

    return result


n = int(input())

sum_divisor = 0
for i in range(1, n + 1):
    divisor = get_divisor(i)
    # print(divisor)
    sum_divisor += sum(divisor)

print(sum_divisor)
"""

# 개선된 풀이
def sum_divisor(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (n // i) * i
    return sum


n = int(input())
answer = sum_divisor(n)

print(answer)
