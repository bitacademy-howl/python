lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned = list()

for i in lst:
    if type(i) == int or type(i) == float:
        lst_cleaned.append(i)

print(lst_cleaned)
