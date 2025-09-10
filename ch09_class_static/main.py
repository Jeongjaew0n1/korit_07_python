'''
기본 예제
가방을 만들 때마다 현재 만들어진 가방이 몇개인지 계산할 수 있는 Bag 클래스를 정의
'''
# # 클래스 정의
# class Bag:
#     # 클래스 변수의 선언 및 초기화
#     count = 0
#     def __init__(self): # 생성자 호출 및 인스턴스 변수들 정의할 용도. 그럼 생성자도 인스턴스 변수라고 할 수 있음.
#         Bag.count += 1 # 생성자가 호출될 때마다(=객체가 생성될 때마다) 클래스 변수인 count 증가. cls.count가 아니라 클래스명.count라는 것에 주목
#         print('가방 객체가 생성되었습니다.')
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#         # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기 때문에 Bag.count가 아니라 cls.count로 작성
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print(f'현재 가방 재고 : {Bag.count}')
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
#
# # 객체 생성
# bag1 = Bag()
# print(f'현재 가장 재고 : {Bag.remain_bag()}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# bag1.sell()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# Bag.sell()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')

'''
다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성
man = Person('김일')
woman = Person('김이')

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회
print(f'전체 인구수 : {Person.get_population()}')

4. man 인스턴스가 삭제되면 다음과 같은 메시지 출력
RIP 김일
'''
# class Person:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         print(f'{name}이(가) 태어났습니다.')
#         Person.population += 1
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     def __del__(self):
#         print(f'RIP {self.name}')
#         Person.population -= 1
#
# man = Person('김일')
# woman = Person('김이')
# print(f'전체 인구수 : {Person.get_population()}')
# del man
# print(f'전체 인구수 : {Person.get_population()}')
# print('프로그램 종료')

'''
가게의 매출을 구할 수 있는 Shop 클래스 작성
1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 가진 list
    menu_list =[{'떡볶이' : 3000}, {'순대' : 4000},
                {'튀김' : 500}, {'김밥' : 2000}]
2. 매출이 생기면 판매량 작성
Shop.sales('떡볶이', 1) # 떡볶이를 1개 판매
Shop.sales('김밥', 2) # 김밥을 2개 판매
Shop.sales('튀김', 5) # 튀김을 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 매출액 확인
print(f'매출 : {Shop.get_total()}원')
'''
class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대': 4000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls, menu_name, count):
        price = 0
        for menu in cls.menu_list:
            if menu_name in menu:
                price = menu[menu_name]
                print(f'{menu_name}을(를) {count}개 판매')
                break
        cls.total += price * count

    @classmethod
    def get_total(cls):
        return cls.total

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print(f'매출 : {Shop.get_total()}원')

