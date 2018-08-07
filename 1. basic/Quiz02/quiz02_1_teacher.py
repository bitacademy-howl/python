# 수를 입력 받음

while True:
    num = input("수를 입력 하세요 : ")

    if num.isdigit():
        break

    print("정수가 아닙니다. 다시 입력하세요.")

total = 0
to = int(num)

for i in range(1, to + 1):
    if i % 3 == 0:
        total += i

print("1부터 {}까지 3의 배수의 합 = {}".format(to, total))
