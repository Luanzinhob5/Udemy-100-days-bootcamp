#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/berga/Documents/Programação atual/CursoUdemy/day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()
    
with open("/Users/berga/Documents/Programação atual/CursoUdemy/day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

i = 0
for name in names:
    i += 1
    name = name.replace("\n","")
    with open(f"/Users/berga/Documents/Programação atual/CursoUdemy/day24/Mail Merge Project Start/Output/ReadyToSend/new_file{i}",mode="w") as new_file:
        new_file.write(content.replace("[name]",name))
    
