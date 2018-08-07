str = "Life is too short, You need Python"

# 문장에 포함된 알파벳

# list0 = str.split(" ")
# list0 = "".join(list0)
# list0 = list0.split(",")
# print(list0)

# 문자열 치환하여 저장
str0 = str.replace(" ", "")
str0 = str0.replace(",", "")
print("replace 결과 : ", str0)

AlphabetOnly = "".join(str0)
print("공백문자 삽입결과 : ", AlphabetOnly)

numberOfAlphabet = len(AlphabetOnly)
print(numberOfAlphabet)

# 문자열 내의 소문자 변경
str2 = str.lower
print(str2)

#문자열 내 공백과 , 제거
list1 = str.split(" ")
list1 = "".join(list1)
list1 = list1.split(",")
AlphabetOnly = "".join(str0)
print(AlphabetOnly)

# 문자열을 List로 변환한 후 담아보기
# list2 = AlphabetOnly.split("")
# print(list2)
str3 = str.replace(" ", "")
str3 = str3.replace(",", "")
print("replace 결과 : ", str3)

str4 = str3.replace("", " ")
str4 = str4.strip()
print(str4)

list5 = str4.split(" ")
print(list5)

chars = set(list5)
print(chars)

list6 = list(chars)
# list6 = list6.split("")
print(list6)

list6.sort()
print(list6)
print(len(list6))




lst = [1,2,3,4,5,6,7,8,9,10]

slice1 = lst[3:7]
print(slice1)

slice1.reverse()
print(slice1)

lst[3:7] = slice1
print(lst)