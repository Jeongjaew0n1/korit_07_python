import random
logo = r'''
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                                                   '''
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
lives = 6
word_list = [ "apple", "banana", "orange", "grape", "peach",
    "monkey", "tiger", "zebra", "elephant", "giraffe",
    "river", "mountain", "desert", "forest", "ocean",
    "school", "pencil", "notebook", "teacher", "student",
    "window", "mirror", "kitchen", "bedroom", "bathroom",
    "planet", "galaxy", "comet", "asteroid", "rocket",
    "puzzle", "guitar", "violin", "camera", "painter",
    "doctor", "farmer", "police", "fireman", "pilot",
    "castle", "village", "jungle", "island", "volcano",
    "summer", "winter", "autumn", "spring", "weather" ]
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display.append('_')
end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives} 번 남았습니다.')
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print('정답입니다 !! 💌')
        end_of_game = True
        print(f'정답은 {chosen_word}입니다.')

    # 현재 상황이 콘솔창에 출력돼서 user에게 안내가 가면 좋겠네요
    print(' '.join(display))