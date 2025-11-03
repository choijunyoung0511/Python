result = 0 #초기화

def adder(num): #adder라는 함수정의  타입이 num인 인수를 받음
    global result #전역변수명시
    result += num #전역변수의 현재값을 입력받은 num값을 더하고 그결괄르 다시 result에저장
    return result #현재깢 ㅣ누적된 result값을 호출

print(adder(3)) # adder함수를 호출할떄 3을 입력함. 함수는 3을 반환
print(adder(4)) #함수를 다시 호출해 4를입력 3 + 4 =7 이므로 7반환