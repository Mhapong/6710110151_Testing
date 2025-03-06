def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = alphabet.upper()
    caesar_encrypted = ""

    k = k % 26 

    for char in s:
        if char.isupper():
            new_index = (upper_alphabet.index(char) + k) % 26
            caesar_encrypted += upper_alphabet[new_index]
        elif char.islower():
            new_index = (alphabet.index(char) + k) % 26
            caesar_encrypted += alphabet[new_index]
        else:
            caesar_encrypted += char

    return caesar_encrypted
