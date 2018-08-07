# 문제10.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menuItems = dict()

def addItem(menu, price):
    menuItems.update({menu : price})

def getPrice(menu):
    try:
        return menuItems[menu]
    except KeyError:
        return 0

addItem("오뎅", 300)
addItem("순대", 400)
addItem("만두", 500)

menu = input('메뉴: ')
print('가격: {0}'.format(getPrice(menu)))

# print(menuItems)
