class HousePark:
    lastname = "박" # 클래스 변수 (모든 인스턴스가 공유) [cite: 807]

    def __init__(self, name):
        # 인스턴스 생성 시 이름을 강제하고 fullname을 초기화 [cite: 808, 809]

        self.fullname = self.lastname + name

    def travel(self, where):
        # 박씨네 여행 메소드 (장소만 입력받음) [cite: 810, 811]
        print("%s, %s여행을 가다." % (self.fullname, where))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))

    # 연산자 오버로딩: 덧셈(+) 연산자 사용 시 호출됨 (결혼) [cite: 816, 817]
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

    # 연산자 오버로딩: 뺄셈(-) 연산자 사용 시 호출됨 (이혼) [cite: 818, 819]
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

# HousePark 클래스를 상속받음 [cite: 820]
class HouseKim(HousePark):
    lastname = "김" # 클래스 변수를 '김'으로 덮어씀 (상속받은 속성 변경) [cite: 821]

    # 메소드 오버라이딩: travel 메소드를 재정의하여 day 인수를 추가함 [cite: 822, 823]
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))
        # --- 클래스 정의 (위의 HousePark, HouseKim 코드가 있다고 가정) ---
# --- 클래스 정의 (위의 HousePark, HouseKim 코드가 있다고 가정) ---

# 1. 인스턴스(객체) 생성: __init__ 메소드 자동 호출
pey = HousePark("응용")
juliet = HouseKim("줄리엣")

# 2. travel 메소드 호출 (오버라이딩 확인)
pey.travel("부산")         # HousePark의 travel (장소만) 호출
juliet.travel("부산", 3)   # HouseKim의 오버라이딩된 travel (장소와 일수) 호출

# 3. 일반 메소드 호출
pey.love(juliet)           # love 메소드 호출
pey.fight(juliet)          # fight 메소드 호출

# 4. 연산자 오버로딩 호출
pey + juliet               # 덧셈 연산자 호출 -> __add__ 메소드 실행 (결혼)
pey - juliet               # 뺄셈 연산자 호출 -> __sub__ 메소드 실행 (이혼)