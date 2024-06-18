'''IMPLEMENT CAESER CIPHER
Create a Python program that can encrypt & decrypt text using the Caeser Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.'''

#Importing the String module to incorporate the alphabets
import string

#Creating a string of alphabets
alphabet = string.ascii_letters

#Function to encrypt a message using Caeser Cipher
def caeser_encrypt(msg, shift):
    #Variable initiation to carry the encrypted message
    encrypted_msg = ""

    #For loop to access each character
    for char in msg:
        #Ensurign the character is an alphabet (optional)
        if char.isalpha():
            # new_index = (currect index of the character + shift key/value) % length of the string alphabet
            # len(alphabet) ensures that an uppercase character is substituted by an upper case letter itself and the same for lowercase character.
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            #The new character or the encrypted character as per the new index
            new_char = alphabet[new_index]
            encrypted_msg += new_char
    #Returning the final encrypted message
    return encrypted_msg

#Function to decrypt an encrypted message using Caeser Cipher
def caeser_decrypt(en_msg, shift):
    #Variable initiation to carry the decrypted message
    decrypted_msg = ""

    #For loop to access each character
    for char in en_msg:
        #Ensuring the character is an alphabet (optional)
        if char.isalpha():
            #Calculating the original index of the decrypted character
            #The shift key/value is negative to reverse the process
            og_index = (alphabet.index(char) + shift) % len(alphabet)
            #Generating the original character
            og_char = alphabet[og_index]
            decrypted_msg += og_char
    #Returning the decrypted message
    return decrypted_msg


#Input message & shift values for the encryption function
message = input("Enter message to be encrypted: ")
shift = int(input("Enter shift key/value (Ex: 3): "))
#Printing the encrypted message
encrypted_msg = caeser_encrypt(message, shift)
print("The encrypted message is: ", encrypted_msg)

#Input encrypted message and negative shift values for the decryption function
en_msg = input("Enter the message to be decrypted: ")
shift = int(input("Enter shift/key value (Ex: -3): "))
#Printing the decrypted message
decrypted_msg = caeser_decrypt(en_msg, shift)
print("The decrypted message is: ", decrypted_msg)