Detailed Code

def vigenere_encrypt(text, key):
    encrypted_text = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65  # Get the shift from the key
            shift_base = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            key_index += 1
        else:
            encrypted_text.append(char)  # Non-alphabetic characters are not encrypted

    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65  # Get the shift from the key
            shift_base = 65 if char.isupper() else 97
            decrypted_text.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
            key_index += 1
        else:
            decrypted_text.append(char)  # Non-alphabetic characters are not decrypted

    return ''.join(decrypted_text)
def main():
    print("Advanced Encryption/Decryption Tool - Vigenère Cipher")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice! Please enter 1 or 2.")
        return

    text = input("Enter the message: ")
    key = input("Enter the encryption key (alphabetic): ")

    if not key.isalpha():
        print("Invalid key! The key must contain only alphabetic characters.")
        return

    if choice == '1':
        result = vigenere_encrypt(text, key)
        print(f"Encrypted message: {result}")
    else:
        result = vigenere_decrypt(text, key)
        print(f"Decrypted message: {result}")
if __name__ == "__main__":
    main()
