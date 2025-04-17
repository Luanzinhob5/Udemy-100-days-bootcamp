import random

# Funcao para escolher uma das cartas na lista
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculadora que soma os pontos, verifica se tem um blackjack e muda o valor do A (11 para 1 o contrario)
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Compara a pontuacao do usuario e da maquina, para ver quem ganhou ou perdeu
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, oppponent has a Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win" 
    else:
        return "You lose"

# Funcao para iniciar o jogo
def play_game():
    is_game_over = False
    user_cards = []
    computer_score = -1
    user_score = -1
    computer_cards = []

    #adiciona 2 cartas na lista do usuario e do computador
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While que mantem o jogo funcionando ate is_game_over = True
    while not is_game_over:

        # Manda a pontuacao de cada um para uma variavel
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        #printa as cartas do usuario e a primeira do computador
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers's first card: {computer_cards[0]}")

        # Acaba com o jogo se o usuario ou o computador dar Blackjack, ou se o usuario passar de 21 pontos
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # Se o IF nao acontecer, pergunta se o jogador que outra carta ou terminar a jogada.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Se a pontuacao do computador for menor que 17 e menor que 0 continue adicionando cartas a lista do computador e soma os pontos do computador
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Prints do final do jogo, se o usuario ou a maquina venceram e suas respectivas cartas e pontuacao
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Your final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

#  Pergunta ao usuario se quer terminar o jogo ou continuar a jogar do zero, e repete a funcao do jogo
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
