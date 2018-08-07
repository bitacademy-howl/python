students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

# print(students, students[0], type(students), type(students[0]))
def getCalcuableField(students):
    pass

def setFieldOfTotal(students):
    for student in students:
        total = student.get("total", 0)
        student["total"] =  total
        print(total)

        for key in student.keys():
            if key == "name":
                continue
            elif key == "kor":
                student["total"] += student[key]
                continue
            elif key == "eng":
                student["total"] += student[key]
                continue
            elif key == "math":
                student["total"] += student[key]
                continue
    # sumOfstudent = student["kor"] + student["eng"] + student["math"]

def setFieldOfAverage(students):
    for student in students:
        total = student.get("total", 0)
        average = total / 3
        if average == 0:
            print("Do SetFieldofTotal first")
        else:
            student["Average"] = int(average)

setFieldOfTotal(students)

setFieldOfAverage(students)

print(students)

# 두 학생의 kor, eng, math 합계 점수와 평균을
# 사전 데이터에 "total", "average" 키값으로 넣어 봅시다.