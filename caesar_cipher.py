def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26 # For keys > 26
            start = ord('A') if char.isupper() else ord('a') # Start from ASCII number for a or A depending on casing
            encrypted_char = chr(start + (ord(char) - start + shift) % 26) # Encrypt character
            encrypted_text += encrypted_char # Add to encrypted text
        else:
            encrypted_text += char # For spaces
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(start + (ord(char) - start - shift) % 26) # Subtracting the shift now to reverse encrypted function
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plaintext = "Hello Devon"
key = 30

encrypted = encrypt(plaintext, key)
#print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
#print("Decrypted:", decrypted)

print(decrypt("Wsqi ermqepw kmzi qi fsrivw", 30))