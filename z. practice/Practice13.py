# 문제13
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
#
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
#
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
#
# 실행 결과:
#
# 숫자를 입력하세요: 7
# 결과 값 : 16
#
# 숫자를 입력하세요: 10
# 결과 값 : 30
#
# 숫자를 입력하세요: 11
# 결과 값 : 36

def sumOfEvenOdd(inputNumber):
    result = 0

    if inputNumber%2 == 0:
        for i in range(0, inputNumber+1, 2):
            result += i
    else:
        for i in range(1, inputNumber+1, 2):
            result += i

    return result

def Q13():
    while(True):
        try:
            inputNumber = int(input("숫자를 입력하세요 : "))
            if inputNumber >= 0:
                print("결과 값 : ", sumOfEvenOdd(inputNumber))
            else:
                print("자연수만 입력 가능합니다. with if구문")
        except ValueError:
            print("정수만 입력 가능합니다. with exception")

Q13()