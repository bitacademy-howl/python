

s = ' spam and ham '
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s1 = '<>><<abc><><><defg>><>><'
print(s.strip('<>'))

print(s.center(60))








# 문자형
# 시퀀스형
# 변경 불가(immutable) 자료형이에요

str1 = "Life is too short, you need Python"
str2 = "Welcome Python"

print(type(str1), type(str2))

print(str1, "str?:", isinstance(str1, str))



lines = '''1st line
2nd line
3nd line
4nd line
'''

print(lines.splitlines())

# 여러 줄 문자열
multiline = """
Java
Python
Linux
"""
print(multiline)

# 문자열 ", ' 사용 가능

# print("I said : "Yes"")  # SyntaxError
# solution 1 : 둘다 사용가능하니 구분지어서 사용할까???
# 문자열 내에 쌍따옴표와 홑따옴표가 같이 들어가는 경우 문제발생 여지가 있음
print('I said "Yes"')
# Solution 2 : 
# 이스케이프 문자를 활용하여 구분
print("I said \" Yes\"")


# 문자열의 인덱싱, 슬라이싱, len
print(len(str1))
print(str1[5])

print(str1[5:7])
print(str1[5:])
print(str1[:6])
print(str1[:])

# str1[0] = 'l' #변경 안됨 = 변경 불가 객체
# str1[0:1] = 'l' # 이렇게도 안됨
# 그냥 스트링 자체가 인덱스 접근으로 변경 불가능한 객체임


# 대소문자 관련
# upper() : 전체 대문자
# lower() : 전체 소문자
# swapcase() : 대 <=> 소문자 전환
# capitalize() : 첫 문자 대문자로
# title() : 각 단어의 첫글자를 대문자로

str3 = str1.lower().title() # 메서드 연결(chaining) : 입력된 순서대로 메서드를 수행하도록 나열하여 사용할 수 있다.

print(str3)

# 검색 관련
print("count()", str1.count("short"))  ## 검색어의 갯수
print("find()", str1.find("Python"))   ## 문자열 내 검색
print("find()", str1.find("Life", 6))  ## 6번 인덱스로부터 Life를 검색
print("rfind()", str1.rfind("Life"))   ## 우측으로부터 검색

print("find() 없는 값", str1.find("Java")) ## 찾는 내용이 없으면 -1을 반환

print("index() : ", str1.index("Python"))
# print("index() 없는 값 : ", str1.index("Java"))   ## index는 찾는 값이 없으면 valueError
#Error를 없애려면

print("1 : ", str1.find("Python"))
print("2 : ", str1.index("Python"))

if (str1.find("Java") > 0):
    str1.index("Java")
    pass
else:
    str1.find("java")
    pass


# 분리와 결합
print("====분리와 결합====")
s = "Java and Python and 이희웅"
lines1 = """
Java
Python
Linux
Oracle
"""

print(s.split()) # 공백문자 기준 분리
print(s.split(" and "))

# 합치기
t = s.split(" and ")
print(t)

# 문자열을 넣어서 합치기
print(":".join(t))


s2 = "abc:def:ghi:jkl:123:456"
# : 기준으로 n 개로 분리
print(s2.split(":", 2))
print(s2.split(":", 3))
print(s2.rsplit(":", 2))


s = "Java and Python and 이희웅"
lines1 = """
Java
Python
Linux
Oracle
"""

# 판별 관련
# isdigit() : 숫자의 형태인가
# isalpha() : 알파벳 형태인가
# islower() : 소문자 형태인가
# isupper() : 대문자 형태인가
# isspace() : 공백문자 형태인가
num = input("정수를 입력하세요 : ")

# ## 아래의 코드는 문자열을 입력했을때 문자열을 4번 반복하게 하고, 숫자가 입력되면 곱셉연산을 수행하는 불규칙한 시스템
# 
# result = num * 4
# print("result : ", result)

# # solution 1 : 입력된 수치를 형변환 후 연산수행 - Error

# result = int(num) * 4
# print("result : ", result)

# solution 2 : 

if num.isdigit():
    result = int(num) * 2
    pass
else:
    # print("정수가 아니에요") # or
    result = "정수가 아니에요"
    pass

print(result)