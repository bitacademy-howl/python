# paint.py
# point 를 임포트 하여 사용

from point import Point

p1 = Point(10, 10)
print("Instance Count : ", Point.instance_count)
print("p1 : ", p1)

p2 = Point(20, 20)
print("Instance Count : ", Point.instance_count)
print("p2 : ", p2)


print(repr(p1))
print(repr(p2))

p2_copy = eval(repr(p2))
print("p2_copy : ", p2_copy)

# repr 메시지를 확인
