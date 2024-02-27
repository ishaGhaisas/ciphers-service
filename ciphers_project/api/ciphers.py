def caesar_encode(plain_text, shift):
    cipher_text = ''
    for c in plain_text:
        if c.isalpha():
            if c.islower():
                c_encoded = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            else:
                c_encoded = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            c_encoded = c

        cipher_text += c_encoded

    return cipher_text
