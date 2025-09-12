from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
# 이상의 경우만 작성했을 때, 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼진다

t.shape('turtle')
t.color('yellow')
screen.bgcolor('black')


# 점선 그리는 반복문
# for _ in range(10):
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()

# .left(각도)
# t.left(90)

# 네모 그리는 반복문
# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# 정삼각형 그리는 반복문
# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# 오각형 / 육각형
# for _ in range(5):
#     t.forward(100)
#     t.left(180-108)

# num = int(input('몇각형을 그릴까요 >>> '))
# for _ in range(num):
#     t.forward(100)
#     t.left(360/num)

color_list = ['dark red',
    'peru',
    'dark khaki',
    'sea green',
    'crimson',
    'cornsilk',
    'pale violet red',
    'dark slate blue',
    'royal blue',
    'papaya whip',
    'khaki',
    'dark sea green',
    'CornflowerBlue',
    'DarkOrchid',
    'IndianRed',
    'DeepSkyBlue',
    'LightSeaGreen',
    'wheat',
    'SlateGray',
    'SeaGreen',
    'tomato',
    'dark olive green',
    'mint cream',
    'sienna',
    'light yellow']
# 도형마다 색 다르게하기
# for i in range(3,11):
#     t.color(random.choice(color_list))
#     for j in range(i):
#         t.forward(50)
#         t.left(360/i)

# 선마다 색 다르게하기
# color_list = ['red','orange','yellow','green','white','purple']
# for i in range(3,11):
#     for j in range(i):
#         t.forward(50)
#         t.left(360/i)
#         t.color(random.choice(color_list))

# def draw_shape(n):
#     for _ in range(n):
#         t.forward(50)
#         t.left(360/n)

# def draw_dotted_line():
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()

# def draw_dotted_shape(n):
#     for _ in range(n):
#         draw_dotted_line()
#         t.left(360/n)
#     t.color(random.choice(color_list))

# for i in range(3,11):
#     draw_dotted_shape(i)
# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())

# .heading의 return 값은 float
# .setheading의 parameter가 float / return None

# t.setheading(t.heading() + 100)
t.speed(0) # 0이 제일 빠름
# for _ in range(36):
#     t.color(random.choice(color_list))
#     t.circle(100)
#     t.setheading(t.heading() + 10)

# 함수화를 위한 일반식을 main에 작성
# n = 10
# for _ in range(n):
#     t.color(random.choice(color_list))
#     t.circle(100)
#     t.setheading(t.heading() + (360 / n))

# 함수화
# def draw_springraph(size_of_gap):
#     for _ in range(100 // size_of_gap):
#         t.color(random.choice(color_list))
#         t.circle(100)
#         t.setheading(t.heading() + (360 / size_of_gap))
# draw_springraph(360)
'''
이상의 코드에서의 문제점은
1. 매개변수인 size_of_gap은 n번째 원과 n+1번째 원의 각도 차이를 나타내는 것인데, 현재로는 반복횟수를 통제하고 있음
2. 360을 입력했을 때, 제자리에서 원이 생성되는 것이 아니라, 그냥 360번을 돌고 있음
'''
# draw_springraph(1)




screen.exitonclick()