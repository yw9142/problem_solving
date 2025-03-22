import sys

def eratos(n):
    # 0, 1은 소수가 아니므로 False로 처리
    num = [False, False] + [True] * (n - 1)

    # 제곱근까지만 확인
    for i in range(2, int(n**0.5) + 1):
        if num[i]:
            # i*i부터 시작하여 중복 제거
            for j in range(i*i, n + 1, i):
                num[j] = False

    # 3부터 시작하는 홀수 소수만 반환 (2는 유일한 짝수 소수)
    return [i for i in range(3, n + 1, 2) if num[i]]

case = []

while True:
    even = int(sys.stdin.readline())
    if even == 0:
        break
    case.append(even)

primes = eratos(max(case))

# print(case) # 4보다 큰 짝수
# print(primes) # 홀수 소수
prime_set = set(primes)

# 조건: 짝수 = 홀수 소수 + 홀수 소수

for i in case:
    found = False
    for j in primes:
        if j > i // 2: # i/2보다 큰 소수는 이미 검사한 내용이라 패스 (중복제거)
            break
        if (i-j) in prime_set: # i - j도 소수인 경우
            print(f"{i} = {j} + {i - j}")
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")


# 왜 안되나 했는데 입력을 sys.stdin.readline()으로 받아야 했다. input()으로 받으면 시간초과가 뜬다. 아..