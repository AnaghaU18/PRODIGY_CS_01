'''IMPLEMENT CAESER CIPHER
Create a Python program that can encrypt & decrypt text using the Caeser Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.'''

#Importing the String module to incorporate the alphabets
import string

#Creating a string of alphabets
alphabet = string.ascii_letters

def caesar_cipher(message, shift):
    final_message = ""

    for char in message:
        if char.isalpha:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            new_char = alphabet[new_index]
            final_message += new_char
    return final_message

def main():
    """
    Prompts the user for input, performs encryption or decryption, and prints the results.
    """
    print("Welcome to the Caesar Cipher program!")

    while True:
        print("Options:")
        print("a) Encrypt")
        print("b) Decrypt")
        print("c) Cancel")

        opt = input("Enter your choice (a-c): ").lower()

        if opt in ("a", "b"):
            message = input("Enter your message: ")
            try:
                # Ensure valid integer input for shift value
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            if opt == "a":
                encrypted_message = caesar_cipher(message, shift)
                print("Encrypted message:", encrypted_message)
            else:
                decrypted_message = caesar_cipher(message, -shift)  # Reverse shift for decryption
                print("Decrypted message:", decrypted_message)

        elif opt == "c":
            print("Thank you for using Caesar Cipher!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
