# 키보드 입력을 받아 비교 및 예외처리,
# 필터링을 담당하는 클래스 등을 정의
class getKeyinput:
    args = print("입력 : ")
    i
    return args




class ExceptionHandler:
    
    def isNumber(args):
        try:
            args.

class Point:
    instance_count = 0 # 클래스 영역

    #생성자
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        # 클래스 영역의 접근
        Point.instance_count += 1
    
    # 소멸자
    def __del__(self):
        Point.instance_count -=1

    # __str__ 구현
    def __str__(self):
        return "Point x = {}, y = {}".format(self.x, self.y)

    # __repr__ 구현
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # 인스턴스 메서드
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y