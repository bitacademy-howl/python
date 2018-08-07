# 논리합 (or) : 둘 중 하나 True 이면 True 반환

a = 2
b = 3

print(a % 2 == 0 or b % 3 == 0)

# 논리곱 (and) : 둘다 true 일때 true 반환

print (a>0 and b<0)   # false
print (a>0 and b>0)   # true
print (a<0 and b<0)   # false

# 논리부정 (not) : 논리값을 반대로 True -> False, False -> True
print("안녕 :", a>10)
print(not a > 10)
print(not a < 10)
print(not(a%2==0 and b%3==0))