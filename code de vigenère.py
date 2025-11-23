from prettytable import PrettyTable
import string


alphabet = string.ascii_uppercase
print (alphabet)

for letter in alphabet:
    indexes = letter.index(f"{letter}")
    print(indexes, end=" ")
    

choice = input("Do you wanna encode or decode a message? ")
if "encode" in choice:
    message = input("What's the message to encode? ")
    key = input("What's the key? ").upper()
else:
    message = input("What's the message to decode? ")
    key = input("What's the key? ").upper()
key_list = list(key)
print(key_list)