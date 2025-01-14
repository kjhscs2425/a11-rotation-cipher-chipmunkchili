import string

alphabet = string.ascii_lowercase
# print(alphabet)

# password = "hi potato zzz"
# # eve wants to steal my password

# # make my password secret
# key = 4

# def encrypt(plaintext):
#     ciphertext = ""
#     for letter in plaintext:
#         old_position = alphabet.find(letter)
#         if old_position == -1:
#             ciphertext += " "
#         else:
#             new_position = old_position + key
#             new_position = new_position % len(alphabet)
#             new_letter = alphabet[new_position]
#             ciphertext += new_letter
#     return ciphertext

# print(encrypt(password))

# Your task:
# figure out what key I used to encrypt this message:
secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"

key = 16

def decrypt(ciphertext):
    plaintext = ""
    for letter in ciphertext:
        new_position = alphabet.find(letter)
        if new_position == -1:
            plaintext += " "
        else:
            old_position = new_position - key
            old_position = old_position % len(alphabet)
            old_letter = alphabet[old_position]
            plaintext += old_letter

    return plaintext

print(decrypt(secret_message))