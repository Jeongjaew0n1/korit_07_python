print("Hello World")
print(1) # 숫자 자료형
print('1') # 문자열 자료형

print(1+2) # 결과값 : 3
print('1'+'2') # 결과값 : 12

print(type('1')) # 결과값 : <class 'str'>
print(type(1)) # 결과값 : <class 'int'>
print(type(1.1)) # 결과값 : <class 'float'>


name = "김일"
age = 20
print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}살입니다.')

name2 = input('이름을 입력하세요 >>> ')
print(name2)