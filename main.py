# ===================================
# [Your Program Title]
# ===================================
# Developed by. [Enter your name]
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
data = [] # Example data model

valid_user = [
    {
        'username': 'admin',
        'password': 'password123',
    }
]

# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for read the data
    """
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the credentials match any valid user
        for user in valid_user:
            if user['username'] == username and user['password'] == password:
                print("Login successful!")
                return True  # Exit and return True if the credentials are correct

        # If no match found after the loop completes
        print("Login unsuccessful. Please try again.")
        return False  # Return False only after all users are checked
# /===== Main Program =====/
# Create your main program here
# Main program loop
while True:
    # Ensure login before allowing access to the menu
    if login():  # Only proceed if the login is successful
        print("Login Sucessfully")
        break
    else:
        # Failed login, retry
        print("Login failed. Please try again.")
        break