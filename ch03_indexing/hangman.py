import random

words = ['apple','banana','grape','orange','strawberry','lemon']

word = random.choice(words)
guess = ['_'] * len(words)
tries = 6

while tries > 0:
    print(' '.join(guess))
    answer = input('알파벳 하나를 입력해주세요 >>> ').lower()
    if answer in word:
        for i in range(len(word)):
            if word[i] == answer:
                guess[i] = answer
        print('알파벳 1개 정답')
    else:
        tries -= 1
        print(f'틀렸습니다. 남은 기회 {tries}번')


