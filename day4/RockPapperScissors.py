import random




rock = "PEDRA"
paper = 'PAPEL'
scissors = "TESOURA"

option = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
computer_option = random.randint(0,2)


game_images = [rock, paper, scissors]

print('Computer choose:',game_images[computer_option])

print('Your choose:',game_images[option])


if option == computer_option:
    print("Draw")

elif option == 0 and computer_option == 1 or option == 1 and computer_option == 2:
    print('You lose')

elif option == 0 and computer_option == 2 or option == 1 and computer_option == 0 or option == 2 and computer_option == 1:
    print('You Win')
    
else:
    print('You choose wrong number')

    

