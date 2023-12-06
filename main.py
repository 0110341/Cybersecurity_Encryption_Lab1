def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = ""

    for char in ciphertext:
        if char.isalpha():
            
            is_upper = char.isupper()
            
            decrypted_char = chr((ord(char) - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            decrypted_message += decrypted_char
        else:
            
            decrypted_message += char

    return decrypted_message

# Example usage
encrypted_message = "Otzkr iutloxsy znk gxxobgr ul znk Kgmrk gz jgct. Ykiaxk znk vgiqgmk gz znk jxuv futk sgxqkj cozn g hrak lrgm. Ktixevz grr yahykwaktz xkvuxzy."
shift_amount = 6
decrypted_message = decrypt_caesar_cipher(encrypted_message, shift_amount)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
