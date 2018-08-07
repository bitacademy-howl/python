
while(True):
    try:
    
        inputdata = int(input("정수를 입력하세요 : "))
        # if type(inputdata)
        if type(inputdata) == int:
            break

    except ValueError as e:
        print("정수가 아닙니다")
        print(e)

    else:
        sumOf = 0
        for i in range(1, inputdata+1):
            if i % 3 == 0:
                sumOf += i
        
        print("1부터 {} 까지의 3의 배수의 합 = {}".format(inputdata, sumOf))