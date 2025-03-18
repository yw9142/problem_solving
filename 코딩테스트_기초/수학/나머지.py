a, b, c = map(int, input().split())

# (a+b) % c
print((a + b) % c)

# ((a%c) + (b%c)) % c
print(((a % c) + (b % c)) % c)

# (a*b) % c
print((a * b) % c)

# ((a%c) * (b%c)) % c
print(((a % c)) * (b % c) % c)
