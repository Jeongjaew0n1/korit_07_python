# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400 , '김오'}
# dict_example = {'이름' : '김일', '나이' : 20, '학교' : '코리아아이티'}

# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dict_example)

# li1 = [10,20,30,40]
# print(li1[0])
# print(li1[1])
# print(li1[2])
# print(li1[-1])
# print(li1[-2])

# li2 = [ 10, 3.04, 'hello'] # 리스트 생성 방법 1
# li3 = list([4, 5, 6, 7, 8, 9, 0]) # 리스트 생성 방법 2
# print(li3[0:4:2])

# scores = [30, 40, 50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0,90)
# print(scores)
# print(scores.pop()) # 근데 .pop()은 call3()유형입니다. 즉 return값이 있는데, 그 삭제한 element가 return 되기 때문에 현재 scores의 마지막 element만 출력
# print(scores.pop(0)) # 결과값 : 첫번째 인덱스 값
# print(scores.remove(50)) # 바로 값을 삭제했기 때문에 None 출력
'''
li4 리스트를 선언하고, 1부터 10까지 값
'''
# li4 = []
# for i in range(1, 11):
#     li4.append(i)
# print(li4)
'''
각 list 내의 element를 뽑아내서 *2 씩
일반 for문
enhance for 형식 첫 번째 element가 4
'''
# for i in range(len(li4)):
#     new_element = li4[i]*2
#     li4[i] = new_element
# print(li4)

# n = 0
# for element in li4:
#     li4[n] = element * 2
#     n += 1
# print(li4)

# 2. tuple

# tu1 = (1, 2, 3) # 튜플 생성 방법 1
# tu2 = tuple((4, 5, 6)) # 튜플 생성 방법 2
# tu3 = 7, 8, 9 # 튜플 생성 방법 3

# a, b, c = 7, 8, 9 # 복수의 변수 선언 및 초기화 방법 -> 즉, 변수 개수와 데이터 개수가 같아야 함
# print(a)
# print(b)
# print(c)

# tu4 = 0 # 그럼 얘의 자료형은 뭘까요
# print(type(tu4)) # int로 나옴
# tu4라고 해서 튜플로 생각하고 변수명을 지었지만 실제로는 그냥 int로 나옴

# tu5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(tu5)

# tu6 = 'hello,', 'good morning', 'my name is', 'kim-il', 'i am' , '20', 'years old'
# for word in tu6:
#     print(word.title(), end=' ') # 결과값 : Hello, Good Morning My Name Is Kim-Il I Am 20 Years Old

# print()
# print(tu6)
'''
이러한 예시를 남겨놓는 이유는 collection의 개념과 내부 element의 자료형이 서로 다르다는 점이기 때문. tuple의 정의는 내부 element의 추가 / 수정 / 삭제가 불가능한 collection이지만. element들은 가공이 가능
가공해서 tuple에 대입하는 것은 불가능 -> 수정이 안되기 때문
'''

'''
3. set
'''
# set1 = {1, 2, 3} # 세트 생성 방법 1
# set2 = set({4, 5, 6}) # 세트 생성 방법 2

# print(set1)
# print(set2)

# 굳이 생성 방법을 나눈 이유 : 비어있는 list / tuple / set 생성 방법
# li = []
# tu = ()
# se = {}

# print(type(li)) # 결과값 : <class 'list'>
# print(type(tu)) # 결과값 : <class 'tuple'>
# print(type(se)) # 결과값 : <class 'dict'>

'''
se = {} 형태로 비어있는 set을 생성했을 경우 se는 사실 dict으로 나옴. 그래서 비어있는 set을 생성하기 위해서는 반드시 첫 번쨰 방식으로 만들어야 함
'''

# se2 = set({}) # 이렇게 만들어야 함
# print(type(se2)) # 결과값 : <class 'set'>

# se3 = {10, 20, 30}
# se3.add(50)
# print(se3) # 순서가 없어서 맨 마지막이 아닌 다른곳에 추가
# se3.remove(30) # 순서가 없기 때문에 '값'을 정확하게 입력해야 함
# print(se3)

# # remove() vs discard()
# # set.remove(70) # 오류 발생 : 값을 정확하게 입력해야만 함
# se3.discard(70) # 얘는 오류가 발생 하지 않음. discard는 element로 정확한 값이 없으면 그냥 종료됨
# print(se3)

# 향상된 for문으로 element를 추출할 수는 있음. 순서를 보장 못할뿐.

'''
4. dict(ionary)
'''
# dict1 = {
#     '이름' : '김일',
#     '나이' : 20,
#     '주소' : ['서울특별시', '마포구', '목동'],
# }

# for key in dict1:
#     print(key)
#     print(dict1[key])

# key들만 추출하는 메서드
# print(dict1.keys()) # 결과값 : dict_keys(['이름', '나이', '주소'])
# print(type(dict1.keys())) # 결과값 : <class 'dict_keys'>

# value들만 추출하는 메서드
# print(dict1.values()) # 결과값 : dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
# print(type(dict1.values())) # 결과값 : <class 'dict_values'>

# key들만 뽑아서 list를 만든다든지 / value들만 뽑아서 list를 만들고 싶다면 형변환 함수를 사용함
# keys = list(dict1.keys())
# value = list(dict1.values())
# print(keys) # 결과값 : ['이름', '나이', '주소']
# print(value) # 결과값 : ['김일', 20, ['서울특별시', '마포구', '목동']]

'''
그래서 collections 수업 상황에서 매우 중요한 것은 list를 배웠을 때 list만 생각할 것이 아니라, set이나 tuple, dictionary로 자료형 변경이 가능한가, 어떤 식으로 가능한가, 어떤 상황에서 사용해야하는가를 같이 종합적인 고려를 하는 역량이 데이터를 다룰 때 중요하다고 할 수 있음
dictionary에서 property 추가 / 삭제
'''
# dict1['직업'] = '웹 퍼블리셔' # 기존에 없던 key를 입력하고 = value 지정
# print(dict1)

# dict1['직업'] = '웹 개발자' # key 하나당 value는 고정이기 때문에 재대입이 이루어짐
# print(dict1)

# 삭제 방법
# print(dict1.pop('직업'))
# print(dict1)

'''
list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그 list에서 2 번쨰 요소를 출력하는 프로그램
실행 예 
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40
'''

# li01 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# li02 = li01[2:7]
# print(f'3 번째 요소로부터 7 번째 요소 = {li02}')
# print(f'3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = {li02[1]}')

'''
사용자로부터 1에서 12까지의 월을 입력 받아, 해당 월이 몇일까지 있는지 출력(윤년은 고려 x)

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지입니다.
'''

# 1 dictionay 이용 방법
# last_date_dict = {
#     '1' : 31,
#     '2' : 28,
#     '3' : 31,
#     '4' : 30,
#     '5' : 31,
#     '6' : 30,
#     '7' : 31,
#     '8' : 31,
#     '9' : 30,
#     '10' : 31,
#     '11' : 30,
#     '12' : 31,
# }
# month = input('1 ~ 12 사이의 월을 입력하세요 >>> ')
# print(f'{month}월은 {last_date_dict[month]}일까지 있습니다.')

# 2
# list01 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
# month01 = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# if month01 >= 1 and month01 <= 12:
#     day = list01[month01 - 1]
#     print(f'{month01}월은 {day}일까지 있습니다.')
# else:
#     print('1에서 12 사이의 값을 입력하세요.')

# 1,3,5,7,8,10,12 -> 31일
# 4,6,9,11 -> 30일

# 3
# list02 = [28, 30, 31]
# month02 = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# if month02 == 2:
#     day = list02[0]
# elif month02 == 4 or month02 == 6 or month02 == 9 or month02 == 11:
#     day = list02[1]
# elif month02 in [1, 3, 5, 7, 8, 10, 12]:
#     day = list02[2]
# else:
#     print('1에서 12 사이의 값을 입력하세요.')
#     day = 'x'
# print(f'{month02}월은 {day}일까지 있습니다.')
'''
in 개념이 중요함.
in 뒤에는 다양한 것들이 올 수 있음. 특히 반복가능객체(iterable)이 올 수 있음.
위의 코드에서 in 다음에 임의의 list를 초기화하여 month02가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토 했다고 볼 수 있음
[1, 3] 대신에 (1, 3) 처럼 초기화 하더라도 상관없음 tuple로 집어 넣는 사례
'''

'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들의 희망하는 모든 수학 여행 장소를 조사
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장
학생을 3명이서 지정하고 실행

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 ['제주', '민속촌']입니다
조사된 수학여행지는 ['제주', '민속촌']입니다
'''

# places_set = set()
# num_place = 3
# for i in range(num_place):
#     place = input('희망하는 수학여행지를 입력하세요 >>> ')
#     places_set.add(place)
# print(set(places_set))

'''
사용자로부터 임의의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램

몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20, 25, 30] 입니다
입력 받은 숫자들 중 짝수는 [10, 20, 30] 입니다.
'''
# nums_list = []
# nums_set = set()
# num = int(input('몇 개의 숫자를 입력할까요? >>> '))
# for i in range(num):
#     nums_list.append(int(input(f'{i+1}번째 숫자를 입력하세요 >>> ')))
#     if nums_list[i] % 2 == 0:
#         nums_set.add(nums_list[i])
# print(f'입력 받은 숫자는 {nums_list}입니다.')
# print(f'입력 받은 숫자들 중 짝수는 {nums_set} 입니다.')

'''
딕셔너리 기반 연락처 관리
사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출

1 번째 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름을 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
...

입력 받은 연락처는 {'김일' : '010-1234-5678' ...} 입니다.
'''
# human_dict = {}
# human_count = 3
# for i in range(human_count):
#     human_key = input(f'{i+1} 번째 사람의 이름을 입력하세요 >>> ')
#     human_value = input(f'{i+1} 번째 사람의 연락처를 입력하세요 >>> ')
#     human_dict[human_key] = human_value
# print(human_dict)

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문졔 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자 추가

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num) - call2() 유형
print(add_numbers2(last_num) - call4() 유형

숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]
예를 들어 hello = ['안', '녕', '하', '세', '요'] 라는 list가 있다고 가정했을 때
add_numbers3(10, hello)를 호출하면
[1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
라는 결과값을 만드는 함수 정의
'''

# numbers1 = []
# def add_numbers1(n):
#     for i in range(n):
#         numbers1.append(i+1)
#     print(numbers1)

# numbers2 = []
# def add_numbers2(n):
#     for i in range(n):
#         numbers2.append(i+1)
#     return numbers2
#
# last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))
# add_numbers1(last_num)
# print(add_numbers2(last_num))

# hello = ['안', '녕', '하', '세', '요']
# numbers3 = []
# def add_numbers3(n, temp_list):
#     for i in range(n):
#         numbers3.append(i+1)
#     for i in range(n):
#         temp_list.insert(i, i + 1)
#     print(temp_list)
# add_numbers3(last_num, hello)

'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수

함수 정의
함수 이름 : count_even_odd()
매개변수 : list_numbers(요소는 모두 정수)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10)]

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''

def count_even_odd(list_numbers):
    count_even = 0
    count_odd = 0
    for i in list_numbers:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f'짝수의 개수 : {count_even}개')
    print(f'홀수의 개수 : {count_odd}개')

count_even_odd([1,2,3,4,5,6,7,8,9,10])
