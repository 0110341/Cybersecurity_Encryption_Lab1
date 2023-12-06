def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = ""

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            decrypted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    return decrypted_message

# Get user input for the message
encrypted_message = input("Type the message: ")

# Get user input for the key
shift_amount = int(input("Type the key (a number): "))

# Decrypt the message
decrypted_message = decrypt_caesar_cipher(encrypted_message, shift_amount)

# Print the results
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

