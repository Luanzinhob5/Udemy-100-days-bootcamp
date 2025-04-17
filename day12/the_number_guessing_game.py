import random
import art 

# Funcao que analisa se o a resposta e maior, menor ou igual ao numero de 1 a 100
def compare(g_uess, n_umber):
    if g_uess == n_umber:
        print(f"You got it! The answer was {number}.")
        return 0
    elif g_uess > n_umber:
        print("Too high.")
    elif g_uess < n_umber:
        print("Too low.")

# Variavel que escolhe um numero de 1 a 100
number = random.randint(1,100)

# Print da logo, das frases iniciais, e input que pergunta a dificuldade
print(f"{art.photo}\n")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# IF que avalia a dificuldade a partir do input difficulty
if difficulty.lower() == "hard":
    lives = 5
else:
    lives = 10

end = 1

# While do jogo, fazendo ele funcionar ate as vidas acabarem ou acertar o numero
while lives > 0 and end != 0:
    print(f"You have {lives} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    end = compare(guess, number)
    if end != 0:
        lives -= 1
    

