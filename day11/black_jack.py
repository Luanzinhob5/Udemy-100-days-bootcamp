import random
''''''
def choose_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def blackjack():
    lista = []
    lista_comp = []
    game = 1

    def win(lista):
        if sum(lista) == 21 and sum(lista) <= 21:
            print(f'    You Win. Score: {sum(lista)}\n      Computer Score: {sum(lista_comp)}')

            return 0

        elif sum(lista) == sum(lista_comp):
            print(f'\n  DRAW. Score: {sum(lista)}\n      Computer Score: {sum(lista_comp)}')
            return 0
    
    def lose(lista):
        if sum(lista_comp) == 21 or sum(lista_comp) > sum(lista) and sum(lista_comp) <= 21:
            print(f'\n    You lose. Score: {sum(lista)}\n      Computer Score: {sum(lista_comp)}')
            return 0
        
        
    def conti():
        cont = input("Type 'y' to get another card, type 'n' to pass: ")
        if cont == 'y':
            lista.append(choose_card())
            win()
        else:
            while sum(lista_comp) < sum(lista) or sum(lista_comp) <= 21:
                lista_comp.append(choose_card())

            if sum(lista) > sum(lista_comp) and sum(lista) <= 21:
                print(f'\n    You Win. Score: {sum(lista)}\n      Computer Score: {sum(lista_comp)}')
            win()
            lose()


    
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    lista.append(choose_card())
    while game == 1:
        if game == 1:
            if start == 'y':
                lista.append(choose_card())
                lista_comp.append(choose_card())

                print(f'    Your cards: {lista}, current score: {sum(lista)}')
                print(f'    Computer first card: {lista_comp}')
                while sum(lista_comp) < sum(lista) or sum(lista_comp) <= 21:
                    lista_comp.append(choose_card())
                win()
                lose()
                if game == 2:
                    break
                else:   
                    conti()
                    
            else:
                game = 2
         
            

blackjack()




