# import random

# def code_msg(message):
#     if len(message) > 3:
#         new_msg = message[1:] + message[0]
#         new_msg = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)) + new_msg + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
#         return new_msg
#     else:
#         return message[::-1] + ''.join(random.choices("abcdefghijklmnopqrstuvwxyz"), k=4)

# def decode_msg(message):
#     if len(message) <= 3:
#         return message[::-1] + message[:-4]
#     else:
#         message = message[3:-6]
#         new_msg = message[-1] + message[:-1]
#         return new_msg

# i = input("Press 'Enter' to start")
# while i.lower() != "\n":
#     choice = input("Enter 'code' to encode message or 'decode' to decode message: ")
#     if choice.lower() == "code":
#         message = input("Enter the message to be encoded: ".lower())
#         encoded_msg = code_msg(message)
#         print("Encoded message:", encoded_msg)
#     elif choice.lower() == "decode":
#         message = input("Enter the message to be decoded: ".lower())
#         decoded_msg = decode_msg(message)
#         print("Decoded message:", decoded_msg)
#     # i = input("Do you want to continue (yes/no)? ")
# print("Goodbye".center(100))


# # this program has problems



# _____________________________________________________________________________________________________________________________________________

import text_speech as tx
import time 
from cryptography.fernet import Fernet
 
message = input("Enter Password: ")
 
# generate a key for encryption and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
 
key = Fernet.generate_key()
 
# Instance the Fernet class with the key
 
fernet = Fernet(key)
 

 
# print("original string: ", message)


# then use the Fernet class instance 
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
 
# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods


 
while True:
    time.sleep(1.5)
    try:
        ask = int(input("What do you want to do? \n 1-Show encrypted string \n 2-Show Decrypted Password \n 3-Quit \n Enter Here→ "))
    except ValueError:
        print("You have entered invalid charater!:\n Please enter [1,2,3] ")
        time.sleep(1)
        ask = int(input("What do you want to do? \n 1-Show encrypted string \n 2-Show Decrypted Password \n 3-Quit \n Enter Here→ "))

    if ask == 1:
        print("Encrypted Password: ", encMessage)
        continue
    elif ask == 2:
        ask_2 = input("Enter the encrypted string: ")
        decMessage = fernet.decrypt(ask_2).decode()
        print("Decrypted Password: ", decMessage)
        continue
    else:
        tx.text_to_speech("Thank You for using")
        exit()