import random
import string

#Password generator processing
def generate(length, digits=True, special_chars=True):
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Set unique password
def unique_passwords(password, pass_set):
    return password not in pass_set

#Save password
def save_passwords(passwords, filename):
    with open(filename, "w") as file:
        file.write("\n".join(passwords))

if __name__ == "__main__":
    print("\n          === Welcome to Password Generator App ===\n")
    pass_set = set()

    while True:
        num_passwords = int(input("How many passwords do you want to generate-: "))
        length = int(input("Enter length of passwords------------------: "))
        digits = input("Include digits (y/n)?------------: ").lower().startswith('y')
        special_chars = input("Include special characters (y/n)?: ").lower().startswith('y')

        generated = []
        while len(generated) < num_passwords:
            password = generate(length, digits, special_chars)
            if unique_passwords(password, pass_set):
                pass_set.add(password)
                generated.append(password)

        print(f"\nGenerated Your {num_passwords} Passwords: ")
        for i, password in enumerate(generated, start = 1):
            print(f"{i}: {password}")

        save_file = input("\nDo you want to save the passwords(yes/no)?----: ").lower()
        if save_file == 'yes':
            filename = input("Enter the filename to save the passwords------: ")
            save_passwords(generated, filename)
            print(f"Passwords saved...file name is----------------: {filename}")

        #More password generate
        Next_regenerate = input("\nDo you want to generate more passwords(yes/no)?: ").lower()
        print("\n")
        if Next_regenerate == 'no':
            print("Thank you for using this App!\n")
            break
