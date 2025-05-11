
# numbers = [1, 2, 3]
# new_list = [item + 1 for item in numbers]

# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# numbers_list = [n * 2 for n in range(1,5)]
# print(numbers_list)

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# short_names = [name for name in names if len(name) < 5 ]
long_names = [name.upper() for name in names if len(name) >= 5 ]
print(long_names)
