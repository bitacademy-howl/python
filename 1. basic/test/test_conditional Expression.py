# 아래는 if else 문을 이용하여 자바나 C의 3항 연산자 개념으로 사용
# value = {true-expr} if {condition} else {false-expr}

# for {타깃} in {객체}:
#     구문 1
#     구문 2
# else :                // for문이 정상종료 되었을 때, 조건문의 finally 와 비슷 개념
#     구문 3            // break로 루프를 빠져나올땐 실행되지 않는다.




i = {1,3,5,7,9,11,12,15}

for val in i :
    if val % 2 == 0 :
        continue
    print(val, end = " ")

