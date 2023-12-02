def encrypt(message, shift):
    # To get the unicode of a character we use the function ord("a")
    # To get the character of a unicode we use the function chr(97)
    shift = shift % 26

    encrypted_message = ""
    for character in message:
        unicode = ord(character)
        shifted_unicode = unicode + shift
        encrypted_character = chr(shifted_unicode)
        encrypted_message += encrypted_character

    return encrypted_message


def decrypt(message, shift):
    shift = shift % 26
    decrypted_message = ""

    for character in message:
        unicode = ord(character)
        shifted_unicode = unicode - shift
        decrypted_character = chr(shifted_unicode)
        decrypted_message += decrypted_character

    return decrypted_message


if __name__ == '__main__':
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)