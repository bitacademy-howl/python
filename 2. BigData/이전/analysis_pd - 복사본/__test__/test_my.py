# 스칼라 값으로 초기화 할때는 반드시 인덱스가 필요
import pandas as pd

s1 = pd.Series(7, index=['a', 'b', 'c', 'd'])
print(s1)