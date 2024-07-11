def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    :param text: The input text to encrypt or decrypt.
    :param shift: The shift value for the Caesar Cipher.
    :param encrypt: A boolean indicating whether to encrypt or decrypt the text.
    :return: The encrypted or decrypted text.
    """
    if not encrypt:
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
            continue

        text = input("Enter the message: ").strip()
        shift = int(input("Enter the shift value: ").strip())

        if choice == 'E':
            result = caesar_cipher(text, shift, encrypt=True)
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(text, shift, encrypt=False)
            print(f"Decrypted message: {result}")

        again = input("Do you want to process another message? (Y/N): ").strip().upper()
        if again != 'Y':
            break

if __name__ == "__main__":
    main()
