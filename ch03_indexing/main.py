str_example = 'hello, python'
# print(str_example[0])
# print(str_example[1])
# print(str_example[2])
# print(str_example[3])
# print(str_example[4])
# print(str_example[5])
# print(str_example[6])
#
# for alphabet in str_example:
#     print(alphabet, end='')
#
# print(str_example[-1])
# print(str_example[-2])
# print(str_example[-3])

'''
네 자리 숫자를 입력 받아 그 숫자의 맨마지막 자리 숫자를 출력
실행 예
네 자리 숫자를 입력하세요 >>> 2025
맨 마지막 숫자는 5입니다.
맨 마지막 숫자는 5이며, 홀수입니다.
'''
number = input('네 자리 숫자를 입력하세요 >>> ')
print(f'맨 마지막 숫자는 {number[-1]} 입니다.')
if (int(number) % 2 == 0) :
    print(f'맨 마지막 숫자는 {number[-1]}이며. 짝수입니다.')
else :
    print(f'맨 마지막 숫자는 {number[-1]}이며. 홀수입니다.')