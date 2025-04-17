import random
import hangman_words as hw
import hangman_images as hi




# Escolher uma das frutas (palavras)
chosen_word = random.choice(hw.fruits)


clean_word = '_'* len(chosen_word)


game_over = False
correct_letters = []
wrong_letters = []
boneco = 0


# logo do Jogo
print(hi.logo)

# While que controla quando o jogo acaba
while not game_over:

    # Entrada do input do jogo
    print(f'{hi.bonecos[boneco]}\n')
    guess = input(f'Guess a Letter: ')

    # IF que faz aparecer o enunciado se a lista (correct_letters) estiver vazia
    if correct_letters == []:
        print(f'\n\nNumber of letters: {clean_word}\n')

    display = ''    

    
    # For que adiciona letras ao display e á lista correct_letters
    if guess in correct_letters:
        print('\n\nYou already use this letter!')
    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
                
            elif letter in correct_letters :
                display += letter

            else:
                display += '_'
            

    print(display)

    # Para alterar o boneco da forca
    if guess in wrong_letters :
        print('\n\nYou already use this letter!')
    elif guess not in display :
        boneco += 1
        wrong_letters.append(guess)


    # Para quando completar a forca encerrar o jogo
    if  '_'  not in display :
        game_over = True
        print(f'\nYOU WIN\nThe word is: {chosen_word}')

    # Para quando completar o boneco encerrar o jogo
    if boneco == 5:
        game_over = True
        print(f'{hi.bonecos[5]}\nYOU LOSE\nThe word is: {chosen_word}')
    
    

