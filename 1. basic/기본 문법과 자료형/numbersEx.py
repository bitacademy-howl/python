# 수치형 연습

# 정수형 : int, 10진, 2진, 8진, 16진 정수를 표현
a = 2018
b = 0b001101
b1 = 0b1101
c = 0o23
d = 0xFF

# print(type(a, b, b1, c, d))
print (type(b), type(b1), type(c), type(d))

print("전체 출력 : ", a, b, b1, c, d)

print("바이너리 옥텟 헥사 (a) : ", bin(a), oct(a), hex(a))

# print("b와 b1의 길이 비교 : ", memoryview(b), memoryview(b1))

print("===========float=============")
x = 1.2345
print(type(a))

print(isinstance(a, float))
print(x.is_integer())

y = 2.0
print(type(y))
print(y.is_integer())


# 복소수

cpx = 4+5j
cpx2 = complex(4,5)

print(cpx, type(cpx))
print(isinstance(cpx, complex))

print(cpx, "\n", "real : ", cpx.real, "\n" "image : ", cpx.imag)

print(cpx.conjugate())

print(cpx == cpx2)

# 내장 수치 함수
print("========수치함수==========")
# 절대값
print(abs(5), abs(-5))
# 정수로 변환
t = int(3.14159)
print(a, int("1234512345"))

# print(int("python")) # 정수가 아닌 다른 문자열은 ValueError 발생

# 실수로 변환 : float
print(float(3), float("3.15151423"))
# print(float("python.0")) # 마찬가지의 ValueError

# x op = y #