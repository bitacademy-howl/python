#fomat_ex.py
# 문자열 서식

# 서식 문자
'''
%s : 문자열
%d : 정수
%f : 부동소수
%% : %리터럴
'''

format = "I have %d apples"
print(format % 10)

print("Interest Rate is %.2f%%" % 1.24)

# 두 개 이상의 값을 넣고 싶을 때
format = "total : %d개, get : %d개"
print(format % (10, 3))
# format과 값의 형식이 일치하지 않으면 TypeError 발생

format_str = "I have {} apples, and I ate {} apples"
print(format_str.format(5, 3))

# 서식에 설정한 공간의 개수와 실제 값의 개수가 다르면 IndexError 발생
print(format_str.format(10,3,1)) # 마지막의 하나는 버림

# format_str.format(10)               # Tuple 인덱스 에러
# print(format_str.format(10))

# 이름 기반의 포멧
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format(total = 7, num = 5))

# print(format_str.format(total = 10))   # KeyError: 지정된 키를 넘겨주지 않음

# dict 객체를 이용한 포멧
print(format_str.format_map({"total":5, "num":2}))

dict1 = {"total":8, "num":8}
print(format_str.format_map(dict1))
