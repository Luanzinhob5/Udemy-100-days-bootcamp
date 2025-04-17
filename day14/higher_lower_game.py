import random
from art import logo
from art import vs
from game_data import data

def celebrity():
    dictionary = random.choice(data)
    name = dictionary["name"]
    followers = dictionary["follower_count"]



def who_is_more_famous(followe, followe2):
    if followe > followe2:
        return 'A'
    else:
        return 'B'
    
    
point = 0 

lista_celebridade = []

dictionary = random.choice(data)

name = dictionary['name']
followers = dictionary["follower_count"]
lista_celebridade.append(dictionary["name"])

print(lista_celebridade)
end_game = False


while not end_game :
    dictionary = random.choice(data)
    while dictionary["name"] in lista_celebridade:
        dictionary = random.choice(data)

    name2 = dictionary["name"]
    followers2 = dictionary["follower_count"]
    lista_celebridade += dictionary["name"]

    famous = who_is_more_famous(followers,followers2)

    print(logo)
    print(f"\n\nCompare A: {name}.")
    print(vs)
    print(f"Against B: {name2}")
    guess = input(f"Who has more followers? Type 'A' or 'B': ")


    if guess.upper() == famous:
        point += 1
        followers = followers2
        name = name2
        
    else:
        end_game = True
        print(f'You Lose. Your pontuation: {point}. "A" followers: {followers}, "B" followers: {followers2}')

