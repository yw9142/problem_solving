# 범위의 소수 구하는 데에는 에라토스테네스의 체가 가장 빠르다.

# 그러나 특정 수가 소수인지 아닌지 판별하는 데에는 에라토스테네스의 체보다 빠른 방법이 있다.
# 그 방법은 해당 수의 제곱근까지만 나누어보는 것이다.
# 어떤 수 N이 소수가 아니라면, N = a * b로 나타낼 수 있다. a, b 중 하나는 N의 제곱근보다 작거나 같다.

def eratos(n=1000):
    # 0, 1은 소수가 아니므로 False로 처리
    num = [False, False] + [True] * (n - 1)

    prime = []
    for i in range(2, n + 1): # 2부터 n까지
        if num[i]: # 소수인 경우
            prime.append(i) # 소수 리스트에 추가
            for j in range(2 * i, n + 1, i): # 소수의 배수는 소수가 아니므로 False로 처리
                num[j] = False
    return prime


N = int(input())
num = list(map(int, input().split()))

prime = eratos()
count = 0

for i in num:
    if i in prime:
        count += 1

print(count)
