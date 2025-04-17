# O erro e que o randint conta mais do que existe na lista
from random import randint
dice_images = ["1","2","3","4","5","6"]
dice_num = randint(1,6)
print(dice_images[dice_num])