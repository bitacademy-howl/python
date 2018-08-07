while True:
    a = input("수를 입력하세요 : ")
    print(a, type(a))

    if a.isdigit():
        a = int(a)
        if(a%3 == 0):
            print("3의 배수입니다.")
            break
        elif(a%3 != 0):
            print("3의 배수가 아닙니다.")

    else:
        print("숫자만 입력가능합니다.")