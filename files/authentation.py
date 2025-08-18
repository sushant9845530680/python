user_base ={}
def register_user():
        username = input("Enter your username: ")

        if username in user_base:
            print("Username already exists. Please choose another one.")
        else:
         password = input("Enter your password: ")
         user_base[username] = password
         print("Registration successful!")
    
def login_user():
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in user_base and user_base[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password. Please try again.")

def authentaiton():
     while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

authentaiton()
