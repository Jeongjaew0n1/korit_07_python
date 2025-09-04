# 함수 정의
# def display_name(name):
#     print(f'당신의 이름은 {name}입니다.')
#
# # 함수 호출
# display_name('김일')
#
# def display_name_age(name, age):
#     print(f'당신의 이름은 {name}이고, 나이는 {age}살입니다.')
#
# display_name_age('김이', 30)
# display_name_age(age=23, name='김삼') # keyword argument
'''
우리가 예를 들어 input('이름을 입력하세요 >>> ')을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name = input('이름을 입력하세요 >>> ')이라고 작성해왔습니다.

그러면 여태까지 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있습니다. 파이썬 내장 함수는 이미 정의가 되어있고, 개발자들은 함수 호출만 잘하면 되겠네요.

사용자 정의 함수의 경우 개발자 자신이 함수를 정의하고, 그 후에 호출까지 하는 것까지의 과정이라고 보시면 되겠습니다.

내장 함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는 함수. 사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하세요 >>> ')
# print(eng_name)
'''
이상의 코드는 함수 호출을 해서 그 결과값을 eng_name이라는 변수에 담았다고 볼 수 있습니다.

그리고 어제 저희가 수업한 것처럼 input()의 결과값의 자료형은 str이었죠.
'''
# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
그렇다면 eng_name.upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는 str 자료형에 종속되어있다고 볼 수 있겠습니다.
그리고 그 결과값을 '다시 eng_name'이라는 변수에 담았기 때문에
55번 라인의 결과값과 57번 라인의 결과값이 차이가 생겼네요.
'''

'''
700 원 짜리 음료수를 뽑을 수 잇는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1 ~ call4 중 어떤 유형일지 고민할 필요가 있습니다)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원

힌트 : +, -, *, /, % 는 다 있는건데
// 이게 있습니다

// : 몫 연산자 몫만 int로 가지고 오는 거
'''
# print(5 // 2)  # 결과값 : 2
# print(5 % 2)    # 결과값 : 1

# 일단 메인에서 굴려보고 함수화시키겠습니다
my_money = 3000
drink_price = 700

# # 1 for 문으로 작성
# change = my_money - (drink_price * 음료개수)
# my_money를 기준으로 음료수를 살 수 있는 경우의 수를 고려했을 때 0 ~ 4 개까지 반복문이 5 번 돌아갑니다.
# for i in range(my_money // drink_price + 1):            # argument가 하나 밖에 없다. 한계값
#     print(f'음료수 개수 = {i}개, 잔돈 ={my_money-(drink_price*i)}')

# # 2 while 문으로 작성
# num = 0
# while my_money >= 0:
#     change = my_money-(drink_price*num)
#     print(f'음료수 개수 = {num}개, 잔돈 = {change}')
#     num += 1
#     my_money -= drink_price

# 일단 for 문을 기준으로 함수화시키겠습니다
def vending_machine(money):          # 이거 교재에 있는 무제 가지고 온건데 함수가 명사라는 점에서 별로 마음에 안듭니다.
    drink_price = 700
    for i in range(money // drink_price + 1):
        print(f'음료수 개수 = {i}개, 잔돈 = {my_money - (drink_price * i)}')

vending_machine(3000)

def vending_machine2(money):
    drink_price = 700
    i = 0
    while True:
        change = money - (drink_price*i)
        if change < 0:
            break
        print(f'음료수 개수 = {i}개, 잔돈 = {change}')
        i+=1

vending_machine2(3000)

'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)           # argument가 dan

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
...
3 x 9 = 27
'''
# def multiply(n):
#     # 로직

# dan = int(input('몇 단을 출력하시겠습니까? >>> '))

# for i in range(1, 10):
#     print(f'{dan} x {i} = {dan*i}')

# def multiply(n):
#     for i in range(1, 10):              # in range() 부분 신경써야하는데
#         print(f'{n} x {i} = {n * i}')
#
# multiply(dan)

'''
range() 함수의 parameter 적용 순서
1 개만 있을 때 : 한계값
2 개 있을 때 : 시작값, 한계값
3 개 있을 때 : 시작값, 한계값, 증감값 순서입니다.

그럼 현재 multiyply를 call2() 유형으로 정의했다고 볼 수 있겠습니다.

multiply2()를 call1() 유형으로 정의했을 때

실행 예
몇 단을 출력하시겠습니까? >>> 5
5 x 1 = 5
...
5 x 9 = 45
로 나올 수 있도록 작성하시오.
'''
def multiyply2():
    dan = int(input('몇 단을 출력하시겠습니까? >>> '))     # 지역 변수(scope)
    for i in range(1, 10, 1):
        print(f'{dan} x {i} = {dan*i}')

multiyply2()

# ch05_hangman -> hangman01





