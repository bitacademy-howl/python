# call by value

# call by reference

# referencing of memory

a = 0
b = 1

c = 1

print(hex(id(a)), hex(id(b)), hex(id(c)))

def modifyNumber(a):
    print(a, type(a))
    a=1

modifyNumber(a)
print(a, b, c)

modifyNumber(b)
print(a, b, c)

modifyNumber(c)
print(a, b, c)

print(hex(id(a)), hex(id(b)), hex(id(c)))

a = 40.25
round(a, 0)
