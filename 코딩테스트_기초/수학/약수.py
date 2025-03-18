n_count = int(input())
divisor = list(map(int, input().split()))

# 8 = 2, 4
divisor.sort()

N =divisor[0] * divisor[-1]

print(N)