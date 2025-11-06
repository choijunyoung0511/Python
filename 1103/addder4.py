class FourCal: #클래스 설계도
    def setdata(self, first, second): #사용할 두숫자를 설정
        self.first = first #self.first를 생성하고, 입력받은 first값으로 초기화
        self.second = second #self.second생성하고 ,입력받은 값은 second로 초기화

    def sum(self):#함수정의
        result = self.first + self.second #현재 인스턴스에 저장된 두값을 더함
        return result #값반환

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


# 실행 (PPT 36장)
a = FourCal() #FourCal 클래스로부터 a라는 첫 번째 인스턴스
b = FourCal() #b라는 두 번째 인스턴스를 생성합니다.
a.setdata(4, 2) #$\text{a}$ 객체의 $\text{setdata}$ 메소드를 호출하여 $\text{a.first}=4$, $\text{a.second}=2$로 설정합니다
b.setdata(3, 7) #$\text{b}$ 객체의 $\text{setdata}$ 메소드를 호출하여 $\text{b.first}=3$, $\text{b.second}=7$로 설정합니다.
print(a.sum())  # 6
print(b.div())  # 0.42857142857142855 (3/7의 결과)