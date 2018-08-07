str = "Life is too short, You need Python"

# str = str.lower()
# str = str.replace(" ", "")
# str = str.replace(",", "")
print("1: ", str)

str = str.lower().replace(" ", "").replace(",", "")
print("2: ", str)

lst = list(str)
print("3: ", lst)

chars = set(lst)
print("4: ", chars)

lst1 = list(chars)
print("5: ", lst1)

lst1.sort() ## 디폴트 오름차순
print("6: ", lst1)

print("7: ", len(lst1))