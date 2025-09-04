import random
import hangman_arts
import hangman_word_list

print(hangman_arts.logo)
lives = 6

chosen_word = random.choice(hangman_word_list.word_list)
display = []

for _ in range(len(chosen_word)):
    display.append('_')
end_of_game = False
while not end_of_game:
    print(hangman_arts.stages[lives])
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
            print(hangman_arts.stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print('정답입니다 !! 💌')
        end_of_game = True
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))