#adder3.py
#5-1은 함수와 클래스의 차이점이 중요
#클래스를 이용하면 계산기의 수가 늘어나더라도 인스턴스를 생성하기만 하면됨
#이 코드의 핵심은 전역변수 대신 객체 내부 (self)에 상태(result)를 지정하자
class Calculator: #클래스 정의

    def __init__(self):  #생성자(초기화 메서드)
                         #init은 객체가 만들어질떄 자동으로 호출되는 함수(15,16번쨰줄 참고)
        self.result = 0  #self.result = 0은 0으로 초기화

    def adder(self, num): #adder()은 객체에 저장된 self.result값을 num만큼 더하고
                          #그 결과를 반환,전역변수 대신 self.result로 자신 가리킴

        self.result += num #기존에 객체 안에 저장된 result값에 num을 더함.
        return self.result #더한 결과 반환

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
