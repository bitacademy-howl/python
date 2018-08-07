# 피클 사용을 위한 import
import pickle

def pwritem01():
    f = open("./sample/players.bin", "wb")
    data = {"baseball": 9}
    pickle.dump(data, f)
    f.close()

pwritem01()

def pread01():
    f = open("./sample/players.bin", "rb")
    data = pickle.load(f)
    f.close()
    print(data, type(data))

pread01()

def pwritem02():
    # 복수의 객체 저장
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball": 9}, f, 1)                         # protocol 1
        pickle.dump({"basketball": 5}, f, 2)                       # protocol 2
        pickle.dump({"soccer": 11}, f, pickle.HIGHEST_PROTOCOL)    # protocol 2

pwritem02()

def pread02():
    # 복수의 객체 읽기
    with open("./sample/players.bin", "rb") as f:
        try:
            print(pickle.load(f))
            print(pickle.load(f))
            print(pickle.load(f))
            print(pickle.load(f))
        except EOFError:
            print("파일 끝")

pread02()

def pread03():
    # 복수의 객체 읽기
    with open("./sample/players.bin", "rb") as f:
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break

            data_list.append(data)
        print(data_list)

pread03()