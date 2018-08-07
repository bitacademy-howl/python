# 문제5.
#
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.

def setTheSet(list):

    resultSet = set()
    for i in list:
        resultSet.add(i)
    return resultSet

def setTheOnlyMap(list):
    resultMap = dict()

    for key in list:
        if key in resultMap.keys():
            resultMap[key] += 1
        else:
            resultMap.update({key:1})

    return resultMap

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

resultList = s.upper().replace(",", " ").replace(", ", " ").replace("\n", " ").replace(".", " ").split()
resultList.sort()

# resultSet = setTheSet(resultList)
resultMap = setTheOnlyMap(resultList)

# for key in resultMap.keys():
#     print(key)

for item in resultMap.items():
    print(*item, sep=':')

# for item in resultMap.items():
#     print(item[0], item[1], sep= " : " , end="\n")

# print(*resultMap.items(), sep="\n")
