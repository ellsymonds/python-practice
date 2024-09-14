
"""Create a function which takes the user's message and encodes or decodes it by shifting
the letters by the amount determined by the user"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shift_amount %= len(alphabet)
        output_text += alphabet[shift_amount]
    print(f"Here is the {direction}ed result: {output_text}")


caesar_cipher(text, shift, direction)
