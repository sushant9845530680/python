import hashlib
import re
from datetime import datetime
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def strong_password(password):
#    print(password)
    if len(password)<8:
       return False, "Password must be at least 8 characters long"
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit"
    if not re.search("[!@#$%^&*()_+]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"        

def log_activity(event):
    # timestamp = datetime.now()
    # print(event)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(timestamp)
    with open("activity_log.txt", "a") as f:
        f.write(f"{timestamp} - {event}\n")

def view_log(username):
    print(f"Viewing log for {username}")
    with open("activity_log.txt", "r") as f:
        logs=f.readlines()
        # print(logs)
        users_log= [log.strip() for log in logs if username in log]
        if users_log:
            for log in users_log:
                print(log)
        else:
            print("No logs found for this user")
   
def login_menu(username):
  while True:  
    print("Login menu")
    print("1. View log")
    print("2. logout")
    choice = input("Enter your choice: ")
    # return choice
    if choice == '1':
        view_log(username)
    
    elif choice == '2':
       print("Exiting...")
       break
    else:
        print("Invalid choice. Please try again.")


def user_register():
    username=input("Enter username: ")
    password=input("Enter password: ")
    is_valid, feedback= strong_password(password)
   
    if not is_valid:
        print(feedback)
        return
    hashed_password = hash_password(password)
    with open("user.txt","a") as f:
        f.write(f"{username}:{hashed_password}\n")
        print("User registered successfully")
        log_activity(f"{username} registered")

def user_login():

    username=input("Enter username: ")
    password=input("Enter password: ")
    with open("user.txt","r") as file:
     users = file.readlines()
    #  print(users)
     for user in users:
      stored_usernme, stored_password = user.strip().split(':')
    #   print(stored_usernme, stored_password)
      if username == stored_usernme and hash_password(password) == stored_password:
        print("Login successful")
        log_activity(f"{username} logged in")
        login_menu(username)
        return
     else: 
        print("Invalid username or password")
        log_activity(f"{username} failed to login")


def main():
  while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_register()
        elif choice == '2':
            user_login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()
