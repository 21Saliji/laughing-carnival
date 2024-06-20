 ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def get_clean_message(text):
  """
  Removes non-alphabetic characters from the message.
  """
  cleaned_message = ''.join(char for char in text.lower() if char.isalpha())
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
    offset = ALPHABET.index(key_char)
    index = ALPHABET.find(char)
    new_index = (index + offset * direction) % len(ALPHABET)
    final_message += ALPHABET[new_index]

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

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

print(f'\nEncrypted text: {encrypt(text, custom_key)}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')