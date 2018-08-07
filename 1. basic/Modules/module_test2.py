# module_test2.py

# from ... import

from math import pi, sin, cos, tan
from mymod import pi, add, subtract, multiply

# 모듈명 지정 없이 이름으로만 호출 할 수 있게 된다.
print(pi)

print(add(10, 20))


# 객체 내부에 __module__을 확인하면 그 객체가 어느 모듈에 속해있는지 확인
# add 메서드의 모듈은 무엇인가

# print(add.__module__)

# add 메서드의 객체의 내부 변수와 객체의 목록
print(dir(add.__module__))

# add 객체의 모듈에 있는 subtract 함수를 실행해 봅시다.
# eval : 문자열로 넘겨받은 내용에 대해 실행을 시도

print(eval(add.__module__+".subtract(20,10)"))