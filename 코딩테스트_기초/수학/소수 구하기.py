def eratos(m, n):
    # 0, 1은 소수가 아니므로 False로 처리
    num = [False, False] + [True] * (n - 1)

    prime = []
    for i in range(2, n + 1): # 2부터 n까지
        if num[i]: # 소수인 경우
            if i >= m: # m 이상의 소수만 반환
                prime.append(i) # 소수 리스트에 추가
            for j in range(2 * i, n + 1, i): # 소수의 배수는 소수가 아니므로 False로 처리
                num[j] = False
    return prime # a 이후의 소수만 반환

M, N = map(int, input().split())

primes = eratos(M, N)

for i in primes:
    print(i)
