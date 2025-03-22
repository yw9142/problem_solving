""" 기존 풀이: 메모이제이션
def sum_divisor(n, memo):
    if n in memo:
        return memo[n]

    sum = 0
    for i in range(1, n + 1):
        sum += (n // i) * i
    memo[n] = sum
    return sum


T = int(input())
memo = {}
answer = []

for i in range(T):
    n = int(input())
    answer.append(sum_divisor(n, memo))

for i in answer:
    print(i)
"""

# 미리 최대 치의 값까지 모두 구해서 필요할 경우 찾아서 쓰는 형태
MAX_N = 1000000
divisor_values = [0] * (MAX_N + 1)

for i in range(1, MAX_N + 1): # 1부터 MAX_N까지의 모든 수 i에 대해 반복. i는 약수 역할
    for j in range(1, MAX_N // i + 1): # i의 배수들을 순회 -> f(i) 값의 일부 계산
        divisor_values[i * j] += i # i를 약수로 가지는 모든 수에 i를 더하는 식으로 누적합 계산
    divisor_values[i] += divisor_values[i - 1] # 1부터 MAX_N까지 차례대로 누적하면서 미리 계산

T = int(input())
answer = []

for _ in range(T):
    n = int(input())
    answer.append(divisor_values[n])

for i in answer:
    print(i)
