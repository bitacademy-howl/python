# 사전
# 순서 없고, key-value 매칭 자료형
# len(), in, not in

# 새로운 사전의 생성
d = dict() # empty dict
print(d)
# 방법 2 : {}를 이용하여
d = {}
print(d, type(d))
# 방법3 : key-value arg를 이용하여 만들기
keys = ('one', 'two', "three")
values = (1, 2, 3)
print(d, type(d))

d = dict(zip(keys, values))
print(d, type(d))

# 사전의 키
print("----------------key----------------")

# 변경 불가 자료형을 사용
d = {}
d[10] = "10"
d["baseball"] = 9
d[("kim", 10)] = "학생"

print(d, type(d))

# d[["lee", 30]] = "근로자" # 타입에러

# 사전 메서드
print("--------------- Methods")

d = {"baseball": 9, "soccer": 11, "basketball": 5}
print(d, type(d))

# 키목록 가져오기 : keys()
print(d.keys())
# 값목록 가져오기 : values
print(d.values())
# 키와 값의 쌍의 목록 : items()
print(d.items())

# 값 가져오기
print(d['baseball'])
# print(d["handball"]) # key Error

# 값 가져오기2 : get
print(d.get("handball"))
print(d.get("handball", "?")) # 기본값을 ?

# 값의 삭제 : del 함수
del d["soccer"]
print(d)

# 사전 비우기
d.clear()
print(d)

# 사전의 순회
print("---------------- 순회")

d = {"baseball": 9, "soccer": 11, "basketball": 5}

# 방법 1 : 키값을 순회하면서 받아와서 내용 처리
for key in d:
    print(key, " : ", d[key])
# for key in d.keys():               # 위를 풀어서 쓴 내용
#     print(key, " : ", d[key])

# 방법 2 : 키와 값을 함께 받아와서 활용 : items()
for key, value in d.items():
    print("{0}:{1}".format(key, value), end= " ")
else:
    print()


# 튜플의 리스트로 생성하기
d = dict(one=1, tow=2)
print(d)

tuple1 = ('one', 1)
tuple2 = ('two', 2)
list1 = [tuple1, tuple2]
d = dict(list1)
print(d)


d = {"one":1, "two":2}

a = "one"
b = "two"
c = 1
d = 2

d = {a:c, b:d}

a = "three"   # 튜플이 참조하는 key변수의 값를 바꾼다고 해서 바뀌지 않는다
c = 3         # 튜플이 참조하는 value 변수의 값을 ????!!!!!?!??!?!?!

print(d)

