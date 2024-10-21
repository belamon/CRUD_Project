# ===================================
# [Your Program Title]
# ===================================
# Developed by. [Enter your name]
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
data_lead = [
    {'lead_id': 1, 'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice.johnson@gmail.com', 
     'phone_number': '081234567890', 'company_sector': 'Finance', 'lead_source': 'LinkedIn', 
     'date_created': '2024-09-20', 'sales_rep': 'Sabrina', 'Transaction': 230000},
    
    {'lead_id': 2, 'first_name': 'Bob', 'last_name': 'Smith', 'email': 'bob.smith@example.com', 
     'phone_number': '082145678901', 'company_sector': 'Technology', 'lead_source': 'Facebook', 
     'date_created': '2024-09-21', 'sales_rep': 'Mutiara', 'Transaction': 400000},
    
    {'lead_id': 3, 'first_name': 'Clara', 'last_name': 'Williams', 'email': 'clara.williams@domain.com', 
     'phone_number': '083256789012', 'company_sector': 'Finance', 'lead_source': 'Instagram', 
     'date_created': '2024-09-22', 'sales_rep':'Sabrina', 'Transaction':700000}
]

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

#Read Menu Functon 
def show_data_leads():
    """Function to display the result when the user chooses number 1 on main menu """
    while True:
        print("\n===== Data Leads =====")
        print("1. Show All Data Records")
        print("2. Search Data Records")
        print("3. Back to Main Menu")

        try:
            user_input = int(input("Enter your choice (1-3): "))  # Get user input and convert to an integer
            # if user chooses 1 : Show all data records
            if user_input == 1:
                if len(data_lead) != 0:  # If the list has at least one lead
                    show_list_of_leads() #Call function to display all leads
                else:
                    print("No data available.") #Inform the user if no data exists
            # if user chooses 2: Search for specific record
            elif user_input == 2:
                search_input = input("Enter the company sector you are looking for: ") #Get the sector to search for 
                data_found = False  # Flag to track if the search finds any results

                for data in data_lead: #Loop through the leads to find maches
                    if search_input.strip().lower() in data['company_sector'].strip().lower():  # Case-insensitive search
                        data_found = True
                        details_of_leads([data])  # Display the leads details 
                        break  # Exit the loop once a matching lead is found 
                if not data_found: #If no matching leads were found
                    print("\n********* Company Sector Not Found *************")
                    print("Here are the available company sectors you can search:")
                    print("Finance")
                    print("Technology")
                    print("Real Estate")
            # if user chooses 3: Go back to the main menu 
            elif user_input == 3:
                return  # Return to exit this function and go back to the main menu
            #Invalid choice handling 
            else:
                print("Invalid choice. Please select 1, 2, or 3.") #Inform the user to enter a valid option 
        except ValueError:
            print("Invalid input. Please enter a number.") #inform the user that the input should be a number



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
    

# /===== Additional Functions =====/
def show_list_of_leads(comment="\n============Available Data Leads=============="):
    """Function to display the list of leads after pressing 1 on show_data_leads function"""
    if len(data_lead) > 0:  # check if there are any leads
        print(comment)
        for lead in data_lead:
            print(f"Lead ID = {lead['lead_id']}")
            print(f"First Name = {lead['first_name']}")
            print(f"Last Name = {lead['last_name']}")
            print(f"Email = {lead['email']}")
            print(f"Phone Number = {lead['phone_number']}")
            print(f"Company Sector = {lead['company_sector']}")
            print(f"Lead Source = {lead['lead_source']}")
            print(f"Date Created = {lead['date_created']}")
            print(f"Sales Representation = {lead['sales_rep']}")
            print(f"Transaction = {lead['Transaction']}")  # Corrected line
            print("-------------------------------------")
    else:
        print("No leads available.")
def details_of_leads(data_lead): #dont forget put the parameneter here to call the data  from the list
    """Function to display details of leads when being called after pressing 2 on show_data_leads_function """
    for detail in data_lead:
        print("\n============Available Data Leads==============")
        print(f"Lead ID = {detail['lead_id']}")
        print(f"First Name = {detail['first_name']}")
        print(f"Last Name = {detail['last_name']}")
        print(f"Email = {detail['email']}")
        print(f"Phone Number = {detail['phone_number']}")
        print(f"Company Sector = {detail['company_sector']}")
        print(f"Lead Source = {detail['lead_source']}")
        print(f"Date Created = {detail['date_created']}")
        print(f"Sales Representation = {detail['sales_rep']}")
        print(f"Transaction = {detail['Transaction']}")

# /===== Main Program =====/
# Create your main program here
# Main program loop
while True:
    # Ensure login before allowing access to the menu
    if login():  # Only proceed if the login is successful
        while True:
            menu_choice = main_menu_choice()
            if menu_choice == 1:
                show_data_leads()

        
    else:
        # Failed login, retry
        print("Login failed. Please try again.")
        