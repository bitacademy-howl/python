# module_test.py
# 모듈명을 바꿔 보겠습니다. : as

import math as m

# m이라는 이름으로 math 모듈 사용
print(m.pi)

# 모듈 내 정의된 객체의 이름을 바꾸기
from mymod import add as sumval

print(sumval(10, 20))

# dir 함수
# 해당 객체가 어떤 변수와 메서드를 가지고 있는지 확인
print(dir(m))

