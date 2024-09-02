import hashlib
import os 
import pyfiglet


print()
def display_center(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate left padding to center the text
    left_padding = (terminal_width - len(text)) // 3
    
    # Display text with padding
    print(" " * left_padding + text)

def main():
    text = " >> YM - Crack  <<"
    banner = pyfiglet.figlet_format(text, font="big", width=160)
    display_center(banner)
    display_center("-----------------------------------")
    display_center("--- Made by Eng Youssef Mohamed ---")
    display_center("-----------------------------------")
    display_center("-----------------------------------")
    display_center("---   github.com/Youssef530245  ---")
    display_center("-----------------------------------")
    print() 
    print()
if __name__ == "__main__":
    main()

#_____________________________________________________________________________
#-----------------------------------------------------------------------------
def crack_hash(hash_to_crack, wordlist):
    hash_algorithms = [
        ('md5', hashlib.md5),
        ('sha1', hashlib.sha1),
        ('sha224', hashlib.sha224),
        ('sha256', hashlib.sha256),
        ('sha384', hashlib.sha384),
        ('sha512', hashlib.sha512),
        ('blake2b', hashlib.blake2b),
        ('blake2s', hashlib.blake2s),
    ]

    try:
        with open(wordlist, 'r') as file:
            for line in file:
                word = line.strip()
                for hash_name, hash_algorithm in hash_algorithms:
                    hash_object = hash_algorithm(word.encode())
                    hashed_word = hash_object.hexdigest()
                    
                    if hashed_word == hash_to_crack:
                        print(f"Hash cracked! The plaintext is: {word}")
                        print()
                        print(f"Hash type: {hash_name}")
                        print()
                        return word, hash_name
            print("Failed to crack the hash with any known algorithms.")
    except FileNotFoundError:
        print(f"The wordlist file '{wordlist}' was not found.")
    return None, None

def main():
    hash_to_crack = input("Enter the hash to crack: ").strip()
    print()
    wordlist = input("Enter the path to the wordlist file: ").strip()
    print()

    cracked_word, hash_type = crack_hash(hash_to_crack, wordlist)
    if cracked_word:
        print(f"The hash {hash_to_crack} corresponds to: {cracked_word}")
        print()
        print(f"Hash type: {hash_type}")
        print()
    else:
        print("The hash could not be cracked.")

if __name__ == "__main__":
    main()


