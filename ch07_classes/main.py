class Person:
    # 메서드 정의(함수가 클래스 내에 있음)
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'전화번호 : {self.tel}')
        print(f'주소 : {self.address}')

    def show_info2(self):
        return f'제 이름은 {self.name} 이고, {self.age}살입니다. 연락처는 {self.tel}인데, {self.address}에 살고 있습니다.'

# 객체 생성
# person1 = Person()

# Person 클래스의 메서드 호출
# person1.set_info('김일', 20, '010-1234-5678', '서웉특별시 마포구')
# person1.show_info()

'''
person2 객체를 생성하고, person2.set_info를 활용하여 입력하고 
show_info2()(call3() 유형으로 작성)를 정의하여 출력

실행 예
제 이름은 ~ 이고, ~살입니다.
연락처는 ~인데, ~에 살고 있습니다.
코드실행
print(person2.show_info())
'''
person2 = Person()
person2.set_info('정재원', 123, '010-1234-5678', '부산광역시')
print(person2.show_info2())