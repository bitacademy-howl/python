a = input("수를 입력하세요 : ")
if a.isdigit():
    a = int(a)

    if a%2 == 0:
        print("짝수")
    elif a%2 != 0:
        print("홀수")