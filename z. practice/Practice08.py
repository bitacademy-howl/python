# 문제 8.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
#
# <<실행결과>>
#
# > 1
# > 2
# > 3
# > 4
# > 5
# 평균: 3.0

def getInput():
    inputList = list()

    while(len(inputList) < 5):
        a = input("> ")
        try:
            inputList.append(int(a))
        except ValueError:
            print("정수만 입력 가능합니다")

    return inputList


inputList = getInput()

print("평균 : {0}".format((sum(inputList)/len(inputList))))
