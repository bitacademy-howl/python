# 문자열

# 연결 : +
a = "py" + "thon"
print(a)

# 반복 : *
b = "Python" * 3
print(b)

# 길이 반환 : len()
c = len("Python")
print(c)

# 포함 여부
s = "Python"

# 시퀀스 내에 y가 있는지 여부 반환
# 대소문자 구분
print("y" in s)
print("Y" in s)

# 시퀀스 내에 j가 포함되어 있지 않은지 여부 반환
print("j" not in s)

# 시퀀스 모델의 인덱스 접근
# 순방향
print(s[4])
# 역방향
print(s[-2])

# 시퀀스 모델의 추출
s1 = s[1:5]
print(s1)

# 역인덱스 이용한 추출
print(s[-5:-1])
# 역인덱스 중 슬라이스 가장 처음 부분까지는 그냥 지정 안하면 됨
print(s[-5:])


# print(s.index(s))