class Calculater: #계산기 틀임
    def __init__(self):
        self.result = 0
    def adder(self,num):
        self.result += num
        return self.result
cal1 = Calculater()
cal2 = Calculater()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))