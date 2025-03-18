answer = []

while True:
    try:
        val = int(input())
        initial_value = 1
        while True:
            if initial_value % val == 0:
                answer.append(len(str(initial_value)))
                break
            # 1, 11, 111, 1111 ....
            initial_value = initial_value * 10 + 1
    except EOFError:
        break

for i in answer:
    print(i)
