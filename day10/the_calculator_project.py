
# funcao de subtracao
def subtract(n1, n2):
    return n1 - n2

# funcao de adicao
def add(n1, n2):
    return n1 + n2

# funcao de multiplicacao
def multiply(n1, n2):
    return n1 * n2

# funcao de divisao
def divide(n1, n2):
    return n1 / n2

# dicionario com operacoes matematicas
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/": divide, 
}


end_program = True
numb = 0

while end_program:
    if numb == 0:
        first_number = float(input('Type your first number: '))
        operator = input('Type a mathematical operator ("+", "-", "*", "/"): ')
        next_number = float(input('Type your second number: '))
        operator = operations[f"{operator}"]
        calc = operator(first_number,next_number)
        previous_result = calc

        numb += 1

    else:
        more_calc = input(f"Do you want to continue working with {previous_result}: ")

        if more_calc.lower() == "n":
            numb = 0
        
        else:
            operator = input('Pick an operation:\n+\n-\n*\n/\n ')
            next_number = float(input('Type your next number: '))
            operator = operations[f"{operator}"]

            calc = operator(float(previous_result),next_number)
            
            previous_result = calc
            


    


