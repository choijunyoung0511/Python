# adder3.py
class Calculator: #클래스정의
    def __init__(self): #init매소드정의 이는 객체를 만들떄 자동을 호출되는   초기화 함수
        self.result = 0 # 벙금생성된 인스턴스 그자신을 가리킴

    def adder(self, num):
        self.result += num
        return self.result

# 인스턴스(별개의 계산기) 생성
cal1 = Calculator()
cal2 = Calculator()

# cal1과 cal2는 독립적으로 결과값을 유지함
print(cal1.adder(3)) # 3 ]
print(cal1.adder(4)) # 7
print(cal2.adder(3)) # 3
print(cal2.adder(7)) # 10