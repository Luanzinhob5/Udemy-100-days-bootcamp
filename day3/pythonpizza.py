#Entrada de dados
print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: ')
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

#Variaveis
pizza = 0
addpepes = 2
addpepeml = 3
addcheese = 1

# Pizza sizes and pepperoni on pizza
if size.upper() == 'S':
    pizza += 15
    if pepperoni.upper() == 'Y':
        pizza += 2

elif size.upper() == 'M':
    pizza += 20
    if pepperoni.upper() == 'Y':
        pizza += 3
else:
    pizza += 25
    if pepperoni.upper() == 'Y':
        pizza += 3

#extra cheese on pizza
if extra_cheese.upper() == 'Y':
        pizza += 1
    


print(f'Your final bill is: {pizza}')