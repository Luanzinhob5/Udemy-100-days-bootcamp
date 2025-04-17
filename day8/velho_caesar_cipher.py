# Alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Entrada de dados
direction = input("Type your 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n").lower())


# The encrypt function
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alfabeto.index(letter) + shift_amount

        shifted_position %= len(alfabeto) # 0-25
        cipher_text += alfabeto[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")


# The decrypt function
def decrypt(original_text,shift_amount):
    output_text = ''

    for letter in original_text:
        shifted_position = alfabeto.index(letter) - shift_amount

        shifted_position %= len(alfabeto)
        output_text += alfabeto[shifted_position]
    
    print(f'Here is the decoded result: {output_text}')
    

# Set the code direction to encode or decode
def direction_code(encode_decode):
    if encode_decode == 'encode':
        encrypt(original_text = text,shift_amount = shift)

    else:
        decrypt(original_text = text ,shift_amount = shift)


direction_code(encode_decode = direction)
