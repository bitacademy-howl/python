# sequence_ex2.py

# range : 순차적 정수를 만들어 내는 함수
# 값이 1개 있을 경우 = end : 0 ~ end 미만의 순차적 정수
seq = range(10)
print(seq, type(seq))

# seq = range(0, 10, 1) # 위의 선언과 동일
# print(seq, type(seq))

# 순차 자료형
print(len(seq)) # 길이
print(seq[5])   # 인덱싱
print(seq[3:7]) # 슬라이싱

# for문을 이용한 순환도 가능
for i in seq:
    print(i)

# 거꾸로 가려면 step 값을 음수
for i in range(10, 0, -1) : print(i)

# enumerate 함수
print("------------------ enumerate")

colors = ["red", "blue", "green", "yello"]
# 이 리스트를 모두 출력하려면
for color in colors:
    print(color)

i = 0
for color in colors:
    print("({0}번 색상은 {1}".format(i, color))
    i += 1

# print(enumerate(colors))

for color in enumerate(colors):
    print(color)

for i, color in enumerate(colors):
    print("{0}번 색상은 {1}".format(i, color))



