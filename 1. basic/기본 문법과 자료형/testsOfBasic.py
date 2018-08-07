import calendar

print(calendar.month(2018, 5))

a, b = 10, 20

print (a,b)

a, b = b, a

print (a, b)

import keyword
keyword.kwlist

# False = a : 키워드로 지정된 문자열은 변수로 사용 불가
Dsa = a #이건 가능


# 주의 : 불린 연산자간의 사칙연산이 가능하므로 계산식에 포함 시킬때 주의하자
print(True + True)
print(True + 10 / False)  # 옆은 제로 디비전 에러를 출력..ㅋㅋ

