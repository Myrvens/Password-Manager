from cryptography.fernet import Fernet

# Function to load the encryption key from the 'key.key' file
def load_key():
    # Open the key file in read-binary mode
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Load the encryption key and initialize the Fernet object
key = load_key()
fer = Fernet(key)

# Function to view saved passwords
def view():
    # Open the passwords file in read mode
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # Remove any trailing whitespace or newline characters
            user, passw = data.split("|")  # Split the line into username and encrypted password
            # Decrypt the password and display it to the user
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


# Function to add a new password to the file
def add():
    name = input('Enter the account name: ')  # Prompt user for the account name
    pwd = input("Enter the password: ")  # Prompt user for the password

    # Open the passwords file in append mode and write the encrypted password
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# Main loop to handle user actions
while True:
    # Prompt the user to choose a mode or quit
    mode = input(
        "Would you like to add a new password or view existing ones (type 'view' or 'add'), or press 'q' to quit? ").lower()
    
    if mode == "q":  # Quit the program
        print("Exiting the program. Goodbye!")
        break

    if mode == "view":  # View existing passwords
        print("\nFetching your saved passwords...\n")
        view()
    elif mode == "add":  # Add a new password
        print("\nLet's save a new account and password.\n")
        add()
    else:  # Handle invalid inputs
        print("\nInvalid option. Please type 'view', 'add', or 'q'.\n")
        continue
