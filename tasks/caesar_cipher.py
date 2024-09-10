
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n")
# shift = input("Type the shift number:\n")

def encrypt(original_text, shift_amount):
    original_text = original_text.lower()
    shift_amount = int(shift_amount)

    encrypted_string = ""
    for letter in original_text:
        new_position = alphabet.index(letter) + shift_amount
        new_position %= len(alphabet)
        encrypted_string += alphabet[new_position]
    return f"Here is the encoded result: {encrypted_string}"


