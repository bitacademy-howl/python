# 문제12
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

import math

def Game369(number):
    result = 0

    while(True):
        ans = number % 10
        if ans == 3 or ans == 6 or ans == 9:
            result += 1
        number = int(number / 10)
        if number == 0:
            break
    return result

def gameRange(number):
    for i in range(1, number):
        result = Game369(i)
        if result > 0:
            print(i, "짝"*result)
            continue

def teachersSolution(number):
    for n in range(1, number):
        s = str(n)
        c = s.count('3') + s.count('6') + s.count('9')
        if c < 1:
            continue

        print("{0} {1}".format(s, '짝' * c))


import time

start1 = time.clock()
gameRange(10000)
end1 = time.clock()

start2 = time.clock()
teachersSolution(10000)
end2 = time.clock()


print("gameRange", end1 - start1)
print("teachersSolution", end2 - start2)

# 숫자가 적을때는 비슷한 속도를 내지만 숫자가 클때는 캐릭터의 갯수를 세는 쪽이 많이 빠름
# 메모리에 저장이 빈번해서 그런지는 좀더 해봐야 할것!

# gameRange(10000000) 14.473688008088677
# teachersSolution(10000000) 8.922656536952793

# 실행 결과:
# 3 짝
# 6 짝
# 9 짝
# 13 짝
# 16 짝
# 19 짝
# 23 짝
# 26 짝
# 29 짝
# 30 짝
# 31 짝
# 32 짝
# 33 짝짝
# 34 짝
# 35 짝
# 36 짝짝
# 37 짝
