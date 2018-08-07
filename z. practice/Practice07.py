# 문제7.
# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
#
# <<실행결과>>

# 50000원 : 1개
# 10000원 : 1개
# 5000원: 1개
# 1000원: 2개
# 500원: 1개
# 100원: 3개
# 50원:1개
# 10원:2개
# 5원:1개
# 1원:4개

class Money:
    exchangeMap = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0, 5:0, 1:0}

    def getDict(self):
        return self.exchangeMap

    def exchange (self, input):

        for key in self.exchangeMap.keys():
            self.exchangeMap[key] = int(input/key)
            input = input%key

    def prntMoney(self):
        for each in self.exchangeMap.items():
            print("{0}원 : {1}개".format(each[0], each[1]))

    def advancedPrntMoney(self):
        for each in self.exchangeMap.items():
            if (each[1] != 0):
                print("{0}원 : {1}개".format(each[0], each[1]))


userMoney = int(input("금액 : "))


b = Money
b.exchange(b, userMoney)


# b.prntMoney(b)
b.advancedPrntMoney(b)