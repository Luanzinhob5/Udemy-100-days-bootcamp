# Ramdomisation
import random


# To get a random number in 1 to 10.
'''
random_intenger = random.randint(1, 10)

print(random_intenger)

'''

# To get a random number under 1
'''
random_number_0_to_1 = random.random() * 10

print(random_number_0_to_1)
'''

# To get a float number in 1 to 10
'''
random_float = random.uniform(1,10)

print(random_float)
'''

# To get 0 or 1
random_heads_or_tails = random.randint(0,1)

print(random_heads_or_tails)
if random_heads_or_tails == 0:
    print('Heads')
else:
    print('Tails')