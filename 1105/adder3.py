class Caculater:
    def __init__(self):
        self.result = 0
    def adder(self, num): #num은 값 전달만해준다
        self.result += num
        return  self.result #영구적으로 저장하는 공간


cal1 = Caculater()
cal2 = Caculater()


print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


# 호출 -> self가 가르키는곳 -> 변수에서 연산 ->result에 값저장