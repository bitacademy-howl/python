lst = [1,2,3,4,5,6,7,8,9,10]

slice1 = lst[3:7]
print(slice1)

slice1.reverse()
print(slice1)

lst[3:7] = slice1
print(lst)