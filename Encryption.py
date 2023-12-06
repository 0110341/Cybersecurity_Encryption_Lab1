# def encrypt(message, shift):
#     # To get the unicode of a character we use the function ord("a")
#     # To get the character of a unicode we use the function chr(97)
#     shift = shift % 26
#
#     encrypted_message = ""
#     for character in message:
#         unicode = ord(character)
#         shifted_unicode = unicode + shift
#         encrypted_character = chr(shifted_unicode)
#         encrypted_message += encrypted_character
#
#     return encrypted_message
#
#
# def decrypt(message, shift):
#     shift = shift % 26
#     decrypted_message = ""
#
#     for character in message:
#         unicode = ord(character)
#         shifted_unicode = unicode - shift
#         decrypted_character = chr(shifted_unicode)
#         decrypted_message += decrypted_character
#
#     return decrypted_message
#
#
# if __name__ == '__main__':
#     message = input("Enter a message to encrypt: ")
#     shift = int(input("Enter shift value: "))
#     encrypted_message = encrypt(message, shift)
#     decrypted_message = decrypt(encrypted_message, shift)
#     print("Original Message:", message)
#     print("Encrypted Message:", encrypted_message)
#     print("Decrypted Message:", decrypted_message)

# def encrypt(message, shift):
#     shift = shift % 26
#
#     encrypted_message = ""
#     for character in message:
#         if character.isalpha():  # Check if the character is a letter
#             unicode = ord(character)
#             shifted_unicode = (unicode - ord('A' if character.isupper() else 'a') + shift) % 26 + ord('A' if character.isupper() else 'a')
#             encrypted_character = chr(shifted_unicode)
#             encrypted_message += encrypted_character
#         else:
#             # Keep non-letter characters unchanged
#             encrypted_message += character
#
#     return encrypted_message
#
#
# def decrypt(message, shift):
#     shift = shift % 26
#     decrypted_message = ""
#
#     for character in message:
#         if character.isalpha():  # Check if the character is a letter
#             unicode = ord(character)
#             shifted_unicode = (unicode - ord('A' if character.isupper() else 'a') - shift) % 26 + ord('A' if character.isupper() else 'a')
#             decrypted_character = chr(shifted_unicode)
#             decrypted_message += decrypted_character
#         else:
#             # Keep non-letter characters unchanged
#             decrypted_message += character
#
#     return decrypted_message
#
#
# if __name__ == '__main__':
#     message = input("Enter a message to encrypt: ")
#     shift = int(input("Enter shift value: "))
#     encrypted_message = encrypt(message, shift)
#     decrypted_message = decrypt(encrypted_message, shift)
#     print("Original Message:", message)
#     print("Encrypted Message:", encrypted_message)
#     print("Decrypted Message:", decrypted_message)


def encrypt(message, shift):
    shift = shift % 26

    encrypted_message = ""
    for character in message:
        if character.isalpha():
            unicode = ord(character)
            shifted_unicode = (unicode - ord('A' if character.isupper() else 'a') + shift) % 26 + ord('A' if character.isupper() else 'a')
            encrypted_character = chr(shifted_unicode)
            encrypted_message += encrypted_character
        else:
            encrypted_message += character

    return encrypted_message


def decrypt(message, shift):
    shift = shift % 26
    decrypted_message = ""

    for character in message:
        if character.isalpha():
            unicode = ord(character)
            shifted_unicode = (unicode - ord('A' if character.isupper() else 'a') - shift) % 26 + ord('A' if character.isupper() else 'a')
            decrypted_character = chr(shifted_unicode)
            decrypted_message += decrypted_character
        else:
            decrypted_message += character

    return decrypted_message


def guess_shift(encrypted_message):
    for shift in range(26):
        decrypted_message = decrypt(encrypted_message, shift)
        print(f"Shift {shift}: {decrypted_message}")


if __name__ == '__main__':
    choice = input("Do you want to encrypt (e) or decrypt (d)? ").lower()

    if choice == 'e':
        message = input("Enter a message to encrypt: ")
        shift = int(input("Enter shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)

    elif choice == 'd':
        encrypted_message = input("Enter an encrypted message: ")
        guess_shift(encrypted_message)

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
