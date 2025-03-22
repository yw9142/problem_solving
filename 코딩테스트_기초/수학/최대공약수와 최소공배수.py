# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
def gcd(a, b):  # 최대공약수
    return gcd(b, a % b) if a % b else b

# 최소공배수 = 두 수의 곱 / 최대공약수
def lcm(a, b, gcd_value):  # 최소공배수
    return a * b // gcd_value


num1, num2 = map(int, input().split())
gcd_val = gcd(num1, num2)

print(gcd_val)
print(lcm(num1, num2, gcd_val))
