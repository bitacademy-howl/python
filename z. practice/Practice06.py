# 문제6.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

# 주어진 리스트에서 3의 배수의 개수=> 6
# 주어진 리스트에서 3의 배수의 합=> 150

def multipleOfn(list, num):
    result = []

    for item in list:
        if item%num == 0:
            result.append(item)

    return result, num

def printMethod(args):
    print("주어진 리스트에서 {0}의 배수의 개수 => {1}".format(args[1], len(args[0])))
    print("주어진 리스트에서 {0}의 배수의 합 => {1}".format(args[1], sum(args[0])))

def Question(list):
    printMethod(multipleOfn(list, 3))


result = Question([3,5,1,2,6,8,9,1,2,3,0,-1,-3])
