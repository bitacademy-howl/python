# 리스트 예제

# 리스트 생성 []
l = [1,2,3,4,5,6,7,8,9,10]

print("l : ", l)
print("Type l : ", type(l))


# 인덱스 접근
print("l[0] : ", l[0])

# 리스트의 길이
print("length l : ", len(l))

# 연결
print(l + [11, 12, 13])
print(l)

#슬라이스
print(l[3:6])

# 슬라이스를 이용한 삭제
l[4:6] = []
print(l)

# 주요 메서드들
a = [1,2,3]
print("a : ", a)

if 4 in a:
    print(a.index())
    pass
else:
    print("없어요")
    pass

a.append(4)
print("a: ", a)

a.append(3)
print("a: ", a)

a.insert(3,5)
print("a: ", a)

# 항목 개수 확인
print([1,2,3,1,2,3].count(3))

# 리스트 뒤집기 (역순 정렬)
a.reverse()
print("a:", a)

# 항목의 정렬 : sort (기본은 오름차순 정렬)

a.sort()
print("a:", a)

# a.sort(True)
# print("a:", a)

# 항목의 삭제
a.remove(5)
print("a:", a)
# a.remove(6)   # remove는 에러 발생 (없을 경우)
# print("a:", a)

# 리스트의 확장 : extend
a.extend([5,6,7])
print("a:", a)

