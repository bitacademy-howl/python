# module_test
# 모듈 임포트

import math
import mymod

# 모듈명을 앞에 붙이고 객체를 사용할 수 있게 됩니다.
print(math.pi)
print(mymod.pi)

r = 10
print("Round:", math.pi * r ** 2)
print("Round:", mymod.pi * r ** 2)

# 어떤 모듈이 현재 로드되어 있는가
import sys

# 현재 로드된 모듈의 목록을 출력
print(sys.modules)

# 모듈이 로드되었는가??
modules = sys.modules.keys()

# 특정 모듈 import 여부 확인
print("YES" if "mymod" in modules else "NO")