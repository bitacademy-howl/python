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

for student in students:
    total = student.get("kor") + student.get("eng") + student.get("math")
    average = total / 3

    student["total"] = total
    student["average"] = average

print(students)