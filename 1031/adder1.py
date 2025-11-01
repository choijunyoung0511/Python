result = 0 #result라는 변수를 전역변수로 선언하고 ,처음값을 0으로 지정
def adder(num): #adder라는 이름의 함수를 정의함,num은 함수가 호출될떄 전달받는 입력인자
    global result #함수 안에서도 전역변수 result를 사용하겠다,함수 내부에서 전역변수에 접근
    result += num #전역변수 result값에 num을 더함.
    return result #값 반환
print(adder(3)) #adder(3)호출-> result가 0 -> 3이 더해져 3출력
print(adder(4)) #adder(4)호출-> result가 0 -> 3+4해서 7이 출력

#3
#7
#이렇게  결과값이 출력됨
#result는 게산기의 내부 메모리 같은 역할을 함