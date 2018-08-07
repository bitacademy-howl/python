# 문제11.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
#
# <<실행결과>>
# 0
# 3
# 18


def sum(*args):
    result = 0
    for arg in args:
        try:
            arg = float(arg)
            result += arg
        except ValueError:
            pass
    return result


numberList = list()

while(True):

    numberList.append(input("수를 입력하세요 : "))
    sumation = sum(*numberList)
    print(numberList)
    print("합계 : {0}".format(sumation))
