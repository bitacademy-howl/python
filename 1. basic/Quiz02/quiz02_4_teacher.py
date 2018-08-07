s = "We encourage everyone to contribute to Python. "
# data 정제
s = s.replace(",", "").replace(".","").replace("\n","").upper()

print(s)

summary = {}

## 문자열 자르기
splits = s.split(" ")
print(splits)

for split in splits:
    if split in summary.keys():
        summary[split] +=1
    else:
        summary[split] = 1

for key, value in summary.items():
    print("{} : {}".format(key, value))
    