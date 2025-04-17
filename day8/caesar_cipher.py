import logo_caesar as lc

# Alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Entrada de dados
print(lc.logo)


# Codificador e decodificador de mensagens
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == 'decode':
                shift_amount *= -1

    for letter in original_text:

        if letter not in alfabeto:
            output_text += letter

        else:
            

            shifted_position = alfabeto.index(letter) + shift_amount
            shifted_position %= len(alfabeto) # 0-25
            output_text += alfabeto[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


yes_or_no = 'yes'

# While faz o programa continuar ate receber "no"
while yes_or_no == 'yes':
    direction = input("Type your 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n").lower())

    caesar(text, shift, direction)
    yes_or_no = input('\nWant to continue "yes" or "no"\n').lower()