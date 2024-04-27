# PRODIGY_CS_01

https://github.com/Stranger1298/PRODIGY_CS_01/assets/84931030/b2e1772b-4f9c-4e0c-b5eb-215ba6226294
Caesar Cipher Encryption and Decryption Tool

This Python script provides a simple implementation of the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Usage
Clone the Repository:
bash
Copy code
git clone https://github.com/your_username/caesar-cipher.git
Navigate to the Directory:
bash
Copy code
cd caesar-cipher
Run the Script:
Copy code
python caesar_cipher.py
Features
Encryption: Encrypts a plaintext message using a specified shift value.
Decryption: Decrypts a ciphertext message using the same shift value used for encryption.
How to Use
Encryption:
Enter the plaintext message you want to encrypt.
Specify the shift value (an integer) by which each letter should be shifted.
The encrypted message will be displayed.
Decryption:
Enter the ciphertext message you want to decrypt.
Specify the same shift value that was used for encryption.
The decrypted message will be displayed.
Example
mathematica
Copy code
$ python caesar_cipher2.py

Choose an option:
1. Encrypt
2. Decrypt
Enter your choice: 1

Enter the plaintext: Hello World
Enter the shift value: 3

Encrypted message: Khoor Zruog
mathematica
Copy code
$ python caesar_cipher.py

Choose an option:
1. Encrypt
2. Decrypt
Enter your choice: 2

Enter the ciphertext: Khoor Zruog
Enter the shift value: 3

Decrypted message: Hello World
Note
Only letters are encrypted or decrypted; other characters remain unchanged.
The shift value can be positive or negative.
For best results, use shift values within the range of 0 to 25.
