users = {"user1": "password1", "user2": "password2"}

def in_valid_user(username):
    # Check if the username exists in the users directory
    return username in users

def check_password(username, password):
    # Check if the provided password matches the stored password for the username
    return users.get(username) == password
    
def login():
    # Prompt user for username and password and validate them
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not is_valid_user(usename):
        print("Username and/or password not found.")
        return
    
    if check_password(username, password):
        print("Login successful!")
    else:
        print("Incorrect password.")

# Example usage
login()
