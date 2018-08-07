# loop_ex.py

# for : for ...in (객체)
for i in range(1, 10, 2):
    print(i, end=",")
else:
    print()

# 시퀀스 객체를 이용한 for문
animals = ['dog', 'Cat', 'Cow', 'Tiger']
for animal in animals:
    print(animal, end=",")
else:
    print()


# enumerate를 이용한 루프
for index, value in enumerate(animals):
    print(index, value)

# while 문
# 
sum, i = 0, 0

while i <= 1000:
    sum += i
    i += 1

print("합계는 : ", sum) 

