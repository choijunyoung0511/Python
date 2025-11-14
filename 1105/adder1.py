#이 예제는 전역변수 result를 사용해 결과를 누적함


result = 0

def adder(num):
    global result
    result += num
    return result
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2