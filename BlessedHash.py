from BlessedCrack import HashCracker
from colorama import init
from termcolor import cprint
import argparse

# Initialize colorama
init()

# Print the banner
cprint("""

 ____  _                        _ _   _           _     
| __ )| | ___  ___ ___  ___  __| | | | | __ _ ___| |__  
|  _ \| |/ _ \/ __/ __|/ _ \/ _` | |_| |/ _` / __| '_ \ 
| |_) | |  __/\__ \__ \  __/ (_| |  _  | (_| \__ \ | | |
|____/|_|\___||___/___/\___|\__,_|_| |_|\__,_|___/_| |_|

Version 1.0
Developed by Team Blessed
""", "red")


def main():
    cracker = HashCracker()

    while True:
        print("\nChoose an option:")
        print("1. Crack MD5 hash")
        print("2. Crack SHA-256 hash")
        print("3. Encrypt text using MD5")
        print("4. Encrypt text using SHA-256")
        print("5. Exit")

        choice = input("Enter the option number: ")

        if choice == '1':
            md5_hash = input("Enter MD5 hash: ")
            wordlist_file = input("Enter the full path to the wordlist file: ")
            cracker.crack_md5(md5_hash, wordlist_file)

        elif choice == '2':
            sha256_hash = input("Enter SHA-256 hash: ")
            wordlist_file = input("Enter the full path to the wordlist file: ")
            cracker.crack_sha256(sha256_hash, wordlist_file)

        elif choice == '3':
            plain_text = input("Enter the text you want to encrypt using MD5: ")
            encrypted_md5 = cracker.encrypt_md5(plain_text)
            print(f"[+] Encrypted text (MD5): {encrypted_md5}")

        elif choice == '4':
            plain_text = input("Enter the text you want to encrypt using SHA-256: ")
            encrypted_sha256 = cracker.encrypt_sha256(plain_text)
            print(f"[+] Encrypted text (SHA-256): {encrypted_sha256}")

        elif choice == '5':
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("[-] Invalid option, please try again.")

if __name__ == "__main__":
    main()