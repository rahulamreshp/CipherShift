import pyperclip as pypc
from encryption import encrypt
from decryption import decrypt


def main():
    while True:
        message = input("Enter Your Message : ")
        print()

        while True:
            operation = input("Enter The Mode ('e' for Encryption / 'd' for Decryption) : ").lower()
            if operation in ['e', 'd']:
                break
            else:
                print()
                print("Wrong Input")
                print()
        print()

        if operation == 'e':
            print("ENCRYPTION BEGINS")
            print()
            k = int(input("Enter The Encryption Key: "))
            result = encrypt(message, k)
            print("\nEncryption Complete \n")
            print(f"Encrypted Cipher: {result} ")
        elif operation == 'd':
            print("DECRYPTION BEGINS")
            print()
            k = int(input("Enter The Decryption Key: "))
            result = decrypt(message, k)
            print("\nDecryption Complete \n")
            print(f"Deciphered Message: {result}")
        else:
            exit()
        print()

        while True:
            copy = input(r"Do You Want To Copy The Result To Clipboard ('y' for yes / 'n' for 'no'): ").lower()
            if copy in ['y','n']:
                break
            else:
                print()
                print("Wrong Input")
                print()

        if copy == 'y':
            pypc.copy(result)
            print("Copied To Clipboard Successfully")
        print()

        while True:
            restart = input("Do you want to restart the operation? ('y' for yes / 'n' for 'no'): ").lower()
            if restart in ['y', 'n']:
                break
            else:
                print()
                print("Wrong Input")
                print()

        if restart != 'y':
            print()
            print("Operation Ended")
            exit()


if __name__ == "__main__":
    main()
