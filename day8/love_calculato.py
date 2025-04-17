def calculate_love_score(name1,name2):
    love = 0
    true = 0
    
    for letter in name1.lower() :
        if letter in 'love':
            love += 1
        if letter in 'true':
            true += 1
    for letter in name2.lower():
        if letter in 'love':
            love += 1
        if letter in 'true':
            true += 1
    print(str(true) + str(love))

calculate_love_score('Kanye West',"Kim Kardashian")