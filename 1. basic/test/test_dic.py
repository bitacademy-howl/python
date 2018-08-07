# d = {"one":1, "two":2}
import copy

a = "one"
b = "two"
c = 1
d = 2

d = {a:c, b:d}

# a = "three"           # 튜플이 참조하는 key변수의 값를 바꾼다고 해서 바뀌지 않는다 --> key 값은 변할 수 없다
c = 3                   # 튜플을 생성할 때 참조한 변수의 값을 바꾼다고 해서 바뀌지 않는다
                        # dict 를 생성할 때는 reference를 참조하는 새로운 객체를 생성하는 것이 아닌
                        # deepcopy로 전혀 새로운 값을 가지는 dictionary를 생성하는 것!

                        ## ㄴㄴ dict 는 튜플의 집합이기 때문에 dict 자체가 callbyref로 동작하지 않는다
                        ## 튜플은 변경 불가 객체


d[a] = 3              # dict이 참조하는 value 변수의 값을 ????!!!!!?!??!?!?!
                      # 바꾸고 싶다면 dict[key]로 접근하여 dict 자체를 바꾸어야 한다.
                      # 한번 생성될 때 참조한 변수의 refrence를 참조하는 것이 아님

print(d)



a1, a2, a3 = 1, 2, 3
a = [a1, a2, a3]
b = copy.deepcopy(a)
print(a)
print(b)

a1 = 4
print(a)