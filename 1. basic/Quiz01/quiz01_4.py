import calendar
# Q4
# 2018년 1월 2일 ~ 1월 5일 사이의 KOSPI 종가는 다음과 같습니다.
# +------------+-----+-----------+
# | date       | dow | price     |
# +------------+-----+-----------+
# | 2018.01.05 | 금  | 2,497.52  |
# | 2018.01.04 | 목  | 2,466.46  |
# | 2018.01.03 | 수  | 2,486.35  |
# | 2018.01.02 | 화  | 2,479.65  |
# +------------+-----+-----------+
# Instruction:

# 리스트 lst_date, lst_dow, lst_price를 만들고 각 항목의 목록을 담아 봅시다.
# kospi_price라는 이름의 빈 사전을 만들어 봅니다.
# dow, price 키값을 보유한 사전을 만들어 kospi_price 사전에 date를 키값으로 추가해 봅시다.
# # 예
# {"dow": "화", "price": 2479.65}
# 2018.01.02를 제외한 나머지 날짜에 price_diff 키를 추가하고 전날의 price와 현재 날짜의 price의 가격 차를 값으로 담아 봅시다.
# 2018.01.05일의 price_diff는 얼마입니까?
# 이 기간 중 최고가와 최저가는 각각 얼마입니까?

lst_date = ["2018.01.05", "2018.01.04", "2018.01.03", "2018.01.02"]
lst_dow = ["금", "목", "수", "화"]
lst_price = [2497.52, 2466.46, 2486.35, 2479.65]


list1 = list()

i = 0
while i < len(lst_date):
    kospi_price = dict()
    kospi_price["dow"] = lst_dow[i]
    kospi_price["price"] = lst_price[i]

    list1.append(kospi_price)
    i += 1
    # kospi_price[dow] = 
    # kospi_price[price] = price
# kospi_price = dict(zip(lst_dow, lst_price))
# kospi_price = zip(lst_dow, lst_price)

print(list1, type(list1))

i = 0
while i < len(list1):
    list1[i]["date"] = lst_date[i]
    i += 1

print(list1, type(list1))

def AddPrice_diff(list1):
    i = 0
    while i < len(list1):
        list1[i]["date"] = lst_date[i]
        i += 1

