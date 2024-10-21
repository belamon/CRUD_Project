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

#Main Menu Function 
def main_menu_choice():
    """Function to display the main menu and get user input"""
    while True: #This will keep asking usert for input until a valid menu option is seleted
        print("\n\t================LEAD MANAGEMENT SYSTEM================")
        print("1. Show Leads")
        print("2. Create Leads")
        print("3. Update Leads")
        print("4. Delete Leads")
        print("5. Check Transaction")
        print("6. Export Report")
        print("7. Exit")

        
        try:
            menu = int(input("Input program menu from (1-7): ")) #menu is the variable to hold menu value 
            if 1 <= menu <= 7:  # check if input is valid between this range
                return menu #return the selected menu option 
            else:
                print("*************** Invalid choice. Please select a number between 1 and 5. ***************")
        except ValueError:
            print("*********** Invalid input. Please enter a valid number between 1 and 5. ************")
            
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
        while True:
            menu_choice = main_menu_choice()

            
    else:
        # Failed login, retry
        print("Login failed. Please try again.")
        