# object_ex.py

print("id 3 : ", id(3))

# 변수에 3을 담는다
# 3 객체를 만들고
#변수에 3객체의 ID를 연결 심볼 테이블에 저장

a = 3
# a의 id값을 확인해 봅시다

print("id a : ", id(a))

b = 3
print("id b : ", id(b))

c = 4
print("id c : ", id(c))

# 객체 심볼 테이블

g_a = 2018
g_b = "symbol"

# 글로벌 영역
def f():               # 로컬 영역 변수 확인을 위한 함수
    l_a = "local"
    l_b = 5
    print(locals())    # 로컬 스코프의 심볼 테이블

print("------------------------ : Local")
f()
print("------------------------ : global")
print(globals())

print("f" in globals().keys())

# 객체 복사
print("---------------------- Object Copy")
x = [1, 2, 3]

# 레퍼런스 복사
y = x
print(x == y)
print(hex(id(x)), hex(id(y)))

x[1] = 4
print(y[1])

# 복제의 시도 : 1

y = x[:]
print("x", x)
print("y", y)

print(x==y)
print(x is y)

x[1] = 0

print(x[1])
print(y[1])

# 복제의 시도 : copy 모듈의 활용
import copy
y = copy.copy(x)
print(x == y)   # 값의 비교   (ex) 자바에서 미리 정의해놓은 equals 함수라고 보면 됨
print(x is y)   # 객체의 비교 (ex) 자비에서 x == y 와 동일

print("x:", x)
print("y:", y)
x[1] = 100
print("x:", x)
print("y:", y)

# 깊은 복제
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]

print("a: ", a)
print("b: ", b)
print("x: ", x)

y = copy.copy(x)
print("y: ", y)

a[1] = 0
print("a: ", a)
print("b: ", b)
print("x: ", x)
print("y: ", y)

# deepcopy
y = copy.deepcopy(x)
print("a: ", a)
print("b: ", b)
print("x: ", x)
print("y: ", y)

a[1] = 100

print("x: ", x)
print("y: ", y)

# deepcopy 는 객체를 다룰 떄 아주 중요하다
