### Caesar Cipher Python Implementation

This Python script implements a Caesar cipher encryption and decryption mechanism using a user-defined key.

#### Usage

The script provides functions for encrypting and decrypting messages using a Caesar cipher with a specified key.

#### Functions

1. **get_clean_message(text)**:
   - Removes non-alphabetic characters from the input text.

2. **generate_key(message, key)**:
   - Repeats the key to match the length of the message.

3. **caesar_cipher(message, key, direction=1)**:
   - Performs Caesar cipher encryption or decryption based on the given direction.
   - **Parameters**:
     - `message`: The message to be encrypted or decrypted.
     - `key`: The key used for encryption or decryption.
     - `direction`: Optional. Default is `1` for encryption, `-1` for decryption.

4. **encrypt(message, key)**:
   - Encrypts the message using the Caesar cipher.

5. **decrypt(message, key)**:
   - Decrypts the message using the Caesar cipher.

#### Example

```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

encrypted_text = encrypt(text, custom_key)
print(f'Encrypted text: {encrypted_text}')
print(f'Key: {custom_key}')

decrypted_text = decrypt(encrypted_text, custom_key)
print(f'Decrypted text: {decrypted_text}')
```

#### Explanation

- **Encryption**: The `encrypt` function encrypts the `text` using the `custom_key` and prints the encrypted text along with the key used.
- **Decryption**: The `decrypt` function decrypts the encrypted text back to its original form using the same `custom_key` and prints the decrypted text.

#### Notes

- The cipher operates only on lowercase alphabetic characters ('a' to 'z').
- Non-alphabetic characters in the input text are ignored during encryption and decryption.

This implementation is straightforward and suitable for basic encryption and decryption tasks using the Caesar cipher method.