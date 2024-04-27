def caesar_cipher(message, key, decrypt=False):
    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in message:
        if char.isalpha():
            shift = key if not decrypt else -key
            idx = alphabet.index(char.lower())
            shifted_idx = (idx + shift) % 26
            shifted_char = alphabet[shifted_idx]
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

message = input("Enter the message: ")
key = int(input("Enter the key (an integer): "))
mode = input("Enter 'encrypt' or 'decrypt': ")
if mode.lower() == 'encrypt':
    encrypted_message = caesar_cipher(message, key)
    print("Encrypted message:", encrypted_message)
elif mode.lower() == 'decrypt':
    decrypted_message = caesar_cipher(message, key, decrypt=True)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
