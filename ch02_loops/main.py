# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1 # python에는 ++가 없음


# 10 부터 1까지 역순으로 출력
# n2 = 10
# while n2 > 0:
#     print(n2)
#     n2 -= 1

'''
중첩 while문 및 f-string을 활용
실행 예
2 x 1 = 2
2 x 2 = 4
'''
n = 2
while n < 10:
    m = 1
    while m < 10:
        print(f'{n} x {m} = {n * m}')
        m += 1
    n += 1

print(n)