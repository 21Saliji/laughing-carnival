ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def get_clean_message(text):
    """
    Removes non-alphabetic characters from the message, preserving spaces.
    """
    cleaned_message = ''.join(char.lower() for char in text if char.isalpha() or char.isspace())
    return cleaned_message

def generate_key(message, key):
    """
    Repeats the key to match the length of the message.
    """
    repeated_key = key * (len(message) // len(key) + 1)
    return repeated_key[:len(message)]

def caesar_cipher(message, key, direction=1):
    """
    Performs Caesar cipher with the given key and direction (encrypt/decrypt).
    """
    cleaned_message = get_clean_message(message)
    repeated_key = generate_key(cleaned_message, key)
    final_message = ''

    for char, key_char in zip(cleaned_message, repeated_key):
        if char.isalpha():  # Only encrypt/decrypt alphabetic characters
            offset = ALPHABET.index(key_char)
            index = ALPHABET.find(char)
            new_index = (index + offset * direction) % len(ALPHABET)
            final_message += ALPHABET[new_index]
        else:
            final_message += char  # Preserve spaces

    return final_message

def encrypt(message, key):
    """
    Encrypts the message using Caesar cipher.
    """
    return caesar_cipher(message, key)

def decrypt(message, key):
    """
    Decrypts the message using Caesar cipher.
    """
    return caesar_cipher(message, key, -1)

def main():
    # Prompt user for input and validate it
    while True:
        text = input('Enter a sentence (only alphabets allowed): ')
        if text.isalpha() or ' ' in text:  # Check if input contains only alphabetic characters or spaces
            break
        else:
            print("Error: Input should contain only alphabetic characters. Please try again.")

    custom_key = 'python'

    encrypted_text = encrypt(text, custom_key)
    print(f'Encrypted text: {encrypted_text}')
    print(f'Key used: {custom_key}')

    decrypted_text = decrypt(encrypted_text, custom_key)
    print(f'Decrypted text: {decrypted_text}')

if __name__ == "__main__":
    main()
