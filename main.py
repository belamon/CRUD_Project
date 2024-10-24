# ===================================
# [Your Program Title]
# ===================================
# Developed by. [Enter your name]
# JCDS - [Class Batch]


# /************************************/
import re
from datetime import datetime
import csv
import pandas as pd
from collections import defaultdict
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
#this is list of sales representation 
valid_sales_reps = ["Sabrina", "Mutiara", "Samantha"]

#this is list of company sector 
valid_sectors = ["Finance", "Technology", "Real Estate"]

#this is list of lead source 
valid_lead_sources = ["LinkedIn", "Facebook", "Instagram"]

#This is list of map month 
months_map = {
        "january": "01", "february": "02", "march": "03", "april": "04",
        "may": "05", "june": "06", "july": "07", "august": "08",
        "september": "09", "october": "10", "november": "11", "december": "12"
    }

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
                print("*************** Invalid choice. Please select a number between 1 and 7. ***************")
        except ValueError:
            print("*********** Invalid input. Please enter a valid number between 1 and 7. ************")

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

#Create menu option 
def create_data_lead():
    """Function to display the result when the user choosing number 2 on main menu """
    while True:
        # Displaying the main menu for creatin a new lead or going back 
        print("\t\t=========CREATE NEW LEAD===============")
        print("1. Create New Lead")
        print("2. Back to Menu")

        try:  # This is a block to handle any invalid input like non-integer values 
            user_input = int(input("Please enter 1 to create a lead or 2 to go back:"))

            if user_input == 1:
                print("===========Input Lead Details===========")

                while True:
                    # Asking user for an email and validate the format
                    while True:
                        lead_email = input("Enter Lead's Email: ") 
                        if validate_email(lead_email):
                            break
                        else:
                            print("Invalid Email Format. Please try again.")

                    # Checking if the email already exists 
                    lead_exists = lead_email in (lead['email'] for lead in data_lead)  # this code is for checking if the email already exists in the list

                    if lead_exists:
                        # If the email already exists, inform the user and display the email
                        print("\t\t=====LEAD DATA CHECK========")
                        print("This email already exists in the database")
                        break

                    #inner loop for checking lead_id
                    while True:
                        try:
                            lead_id = int(input("Enter Lead ID: "))
                            id_exists = lead_id in (lead['lead_id'] for lead in data_lead)
                            if id_exists:
                                print("Lead ID already exists. Please input another Lead ID")
                            else:
                                break #exit the loop if a unique lead is provided
                        except ValueError:  # Handle the case where conversion to int fails
                            print("Invalid input. Please input a number.")
                                      

                    # Collect lead details from the user 
                    first_name = input("Enter First Name of the Lead: ")
                    last_name = input("Enter Last Name of the Lead: ")

                    # Prompt for phone number and validate it 
                    while True:
                        phone_number = input("Enter Phone Number: ")
                        if validate_phone_number(phone_number):
                            break
                    #Prompt company sector and validate it 
                    
                    while True:
                        company_sector = input("Enter Company Sector of the Lead: ")
                        if validate_sector(company_sector):
                            break
                    #Prompt lead source and validate it 
                    while True:
                        lead_source = input("Enter Lead Source of the Lead: ")
                        if validate_source(lead_source):
                            break
                    #Validate the date input    
                    while True:
                        date_created = input("Enter Date Created of the Lead: ")
                        if validate_date(date_created):
                            break
                    #Validate sales representation 
                    while True:
                        sales_rep = input("Enter Sales Representative:")
                        if validate_sales(sales_rep):
                            break

                    while True:
                        try:
                            transaction = int(input("Enter the new Transaction: "))
                            print(f"Transaction updated to: {transaction}")
                            break  # Exit the loop if a valid integer is provided
                        except ValueError:
                            print("Please input a valid number.")  # Inform the user to input a number


                    # Store the lead details in a dictionary 
                    new_lead = {
                        "lead_id": lead_id,
                        "first_name": first_name, 
                        "last_name": last_name,
                        "email": lead_email,
                        "phone_number": phone_number,
                        "company_sector": company_sector,
                        "lead_source": lead_source,
                        "date_created": date_created,
                        "sales_rep":sales_rep,
                        "Transaction":transaction
                    }

                    # Display a confirmation page
                    print("\n=== Confirmation Page ===")
                    print(f"First Name: {first_name}")
                    print(f"Last Name: {last_name}")
                    print(f"Email: {lead_email}")
                    print(f"Phone Number: {phone_number}")
                    print(f"Company Sector: {company_sector}")
                    print(f"Lead Source: {lead_source}")
                    print(f"Date Created: {date_created}")
                    print(f"Sales Representation: {sales_rep}")
                    print(f"Transaction: {transaction}")
                        

                    #Ask for confirmation until a valid input is received 
                    confirm = confirmation_page(action="Save", data=new_lead)
                    if confirm == "1":
                        print("\nLead Added Successfully!")
                        data_lead.append(new_lead)
                        break
                    elif confirm == "2":
                        print("\nLead not added.")
                        break
                    else:
                        print("Invalid input. Please choose between 1 or 2.")


            elif user_input == 2:
                # If user selects 2, then they will return to the main menu 
                print("Returning to the main menu ")
                break  # Exit the loop and back to the main menu 

            else:
                # If user enters a number other than 1 or 2, show an error message 
                print("Invalid Input. Please enter 1 or 2")


        except ValueError:
            print("Invalid Input. Please enter the number between (1-2)")


#Update Data Leads Function 
def update_data_lead():
    """Function to display the result when the user inputs number 3 on the main menu."""
    
    while True:  # Outer loop for updating data leads
        print("\t\t============UPDATE DATA LEADS====================")
        print("1. Update Data Leads")
        print("2. Back to Menu")

        try:
            operation = False
            user_input = int(input("Please Choose an Option (1-2): "))

            if user_input == 1:
                print("===============Input Update Data of The Leads=====================")

                while not operation:  # Inner loop for updating leads
                    lead_email = input("Enter the email of the Lead you want to update: ")
                    lead_found = False

                    for lead in data_lead:
                        if lead["email"] == lead_email:
                            lead_found = True 

                            details_of_leads([lead])  # Display lead details

                            user_confirmation = confirmation_page(action="update", data=lead)  # Re-confirmation

                            if user_confirmation == "1":  # Confirm update
                                # Store original values for confirmation
                                original_lead = lead.copy()  
                                update_made = False  # Flag to track if an update has been made

                                print("Choose column that you want to be updated")
                                print("1. Lead ID ")
                                print("2. First Name")
                                print("3. Last Name")
                                print("4. Email")
                                print("5. Phone Number")
                                print("6. Company Sector")
                                print("7. Lead Source")
                                print("8. Date Created")

                                while True:
                                    try:  # This is a block to get the column that user wants to update
                                        column_choice = int(input("Please Choose an Option (1-8): "))
                                        if column_choice == 1:
                                            lead_id = int(input("Enter the new Lead ID (must be an integer): "))
                                            lead["lead_id"] = lead_id
                                            print(f"Lead ID updated to : {lead_id}")
                                            update_made = True  # Update occurred
                                            break 
                                        elif column_choice == 2:
                                            first_name = input("Enter the new First Name: ")
                                            lead["first_name"] = first_name
                                            print(f"First Name updated to : {first_name}")
                                            update_made = True  # Update occurred
                                            break 
                                        elif column_choice == 3:
                                            last_name = input("Enter the new Last Name: ")
                                            lead["last_name"] = last_name
                                            print(f"Last Name updated to : {last_name}")
                                            update_made = True  # Update occurred
                                            break
                                        elif column_choice == 4:
                                            email = input("Enter the new Email: ")
                                            if validate_email(email):
                                                lead["email"] = email
                                                print(f"Email updated to : {email}")
                                                update_made = True  # Update occurred
                                                break
                                            else:
                                                print("Invalid email format. Please try again.")
                                        elif column_choice == 5:
                                            phone_number = input("Enter the new Phone Number: ")
                                            if validate_phone_number(phone_number):
                                                lead["phone_number"] = phone_number
                                                print(f"Phone Number updated to : {phone_number}")
                                                update_made = True  # Update occurred
                                                break
                                            else:
                                                print("Invalid phone number. Please enter digits only (10-15 characters).")
                                        elif column_choice == 6:
                                            company_sector = input("Enter the new Company Sector: ")
                                            if validate_sector(company_sector):
                                                lead["company_sector"] = company_sector
                                                print(f"Company Sector updated to : {company_sector}")
                                                update_made = True  # Update occurred
                                                break
                                            else:
                                                print(f"Invalid sector. Please choose from the following options: {', '.join(valid_sectors)}")  
                                        elif column_choice == 7:
                                            lead_source = input("Enter the new Lead Source: ")
                                            if validate_source(lead_source):
                                                lead["lead_source"] = lead_source
                                                print(f"Lead Source updated to : {lead_source}")
                                                update_made = True  # Update occurred
                                                break
                                            else:
                                                print(f"Invalid source. Please choose from the following options: {', '.join(valid_lead_sources)}")
                                        elif column_choice == 8:
                                            date_created = input("Enter the new Date Created (YYYY-MM-DD): ")
                                            if validate_date(date_created):
                                                lead["date_created"] = date_created
                                                print(f"Date Created updated to : {date_created}")
                                                update_made = True  # Update occurred
                                                break
                                            else:
                                                print("Invalid date format. Please use YYYY-MM-DD.")
                                        else:
                                            print("Invalid Option. Please choose a valid option (1-8).")
                                    except ValueError:
                                        print("Invalid Input. Please enter a valid number.")
                                        continue

                                # Ask for confirmation to save changes only if an update was made
                                if update_made:
                                    while True:  # Add a loop to keep asking for confirmation
                                        save_confirmation = confirmation_page(action="save", data=lead)
                                        if save_confirmation == "1":  # User confirms save
                                            print("Changes saved successfully.")
                                            operation = True
                                            break  # Break out of the save confirmation loop
                                        elif save_confirmation == "2":  # User cancels save
                                            lead.update(original_lead)  # Revert to original values
                                            print("Changes reverted.")
                                            operation = True 
                                            break  # Break out of the save confirmation loop
                                        else:
                                            print("Invalid Option. Please choose a valid option.")
                                    
                            elif user_confirmation == "2":
                                print("Data update canceled.")
                                break  # Exit the inner loop and go back to the outer loop

                    if not lead_found:
                        print("The data you are looking for does not exist.")

                    # Check if we broke out of the inner loop due to cancellation
                    if not lead_found or user_confirmation == "2":
                        break  # Break the inner loop to go back to the outer menu

            elif user_input == 2:
                return  # Go back to the main menu
            else:
                print("Invalid choice. Please choose 1 or 2.")

        except ValueError:
            print("Invalid input. Please enter a number.")



#Delete data function

deleted_leads = []  # List to hold deleted leads

def delete_data():
    """Function to delete leads based on user input."""
    
    while True:
        print("====DELETE DATA LEAD=====")
        

        # Show options to the user
        print("\nOptions:")
        print("1. Delete lead by email")
        print("2. Restore deleted lead by email")
        print("3. Show deleted leads")
        print("4. Back to Main Menu")

        user_input = input("Enter Choice: ")

        if user_input == "1":  # Delete lead by email
             # Show list of current leads before proceeding
            show_list_of_leads()
            #ask user to input email
            email = input("Enter email of the lead to delete: ")
            
            # Find the lead with the matching email
            lead_found = None
            for lead in data_lead:
                if lead['email'] == email:
                    lead_found = lead  # Store the lead to delete
                    break

            if lead_found:  # If a matching lead was found
                # Confirm deletion
                user_confirmation = confirmation_page(action="delete", data=lead_found)
                if user_confirmation == "1":  # Confirm deletion
                    deleted_leads.append(lead_found)  # Move lead to deleted leads
                    data_lead.remove(lead_found)  # Remove lead from active list
                    print("\nLead successfully deleted.")
                    show_list_of_leads_after_deleted()  # Show updated list of leads
                elif user_confirmation == "2":  # Cancel deletion
                    print("\nLead not deleted.")
            else:
                print("No lead found with the provided email.")

        elif user_input == "2":  # Restore deleted lead by email
            # Show list of deleted leads before proceeding
            show_deleted_leads()
            # Ask user to input email
            email = input("Enter email of the lead to restore: ")
            lead_to_restore = None
            for lead in deleted_leads:
                if lead['email'] == email:
                    lead_to_restore = lead
                    break

            if lead_to_restore:  # If a matching deleted lead was found
                data_lead.append(lead_to_restore)  # Restore the lead to active leads
                deleted_leads.remove(lead_to_restore)  # Remove from deleted leads
                print(f"Lead with email {email} restored successfully.")
            else:
                print("No deleted lead found with the provided email.")

        elif user_input == "3":  # Show deleted leads
            show_deleted_leads()

        elif user_input == "4":  # Back to Main Menu
            return  # Exit back to the main menu

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def show_list_of_leads_after_deleted():
    """Function to display only active leads (leads that are not deleted)."""
    print("===== Active Data Leads =====")
    for lead in data_lead:
        details_of_leads([lead])  # Display details of active leads

def show_deleted_leads():
    """Function to display only deleted leads."""
    if deleted_leads:
        for lead in deleted_leads:
            details_of_leads([lead])  # Display details of deleted leads
    else:
        print("No deleted leads available.")

def confirmation_page(action, data):
    """Mock function for user confirmation."""
    print(f"Are you sure you want to {action} this lead?")
    details_of_leads([data])
    return input("Enter 1 to confirm, 2 to cancel: ")

def details_of_leads(leads):
    """Function to display details of leads."""
    for lead in leads:
        print(f"Lead ID: {lead['lead_id']}, Name: {lead['first_name']} {lead['last_name']}, Email: {lead['email']}")

#Transaction function
def transaction():
    """Function to perform transactions on the data."""
    while True:
        print("\n===== Transaction Menu =====")
        print("1. Filter Month of Transaction")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            month = input("Enter the month name (e.g., 'January'): ").strip().lower()  # Convert to lowercase
            filter_leads_by_month(month)
        elif choice == "2":
            break  # Exit back to the main menu
        else:
            print("Invalid choice. Please select a valid option.")
#report data function 
def report_menu(data_leads):
    while True:
        print("\n==== Reporting Menu ====")
        print("1. Generate Summary Report")
        print("2. Export to CSV")
        print("3. Export to Excel")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            report = generate_summary_report(data_leads)
            print("============Summary Report:===========")
            for sector, count in report.items():
                print(f"{sector}: {count}")
            input("Press enter  to continue...")
        elif choice == "2":
            filename = input("Enter filename for CSV export: ")
            export_to_csv(data_leads, filename)
            input("Press enter  to continue...")
        elif choice == "3":
            filename = input("Enter filename for Excel export: ")
            export_to_excel(data_leads, filename)
            input("Press enter  to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

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

def validate_email(email):
    """
    Function to validate if an email is in the correct format.

    Returns True if valid, False otherwise
    """
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    #user re.match() to check if the email matches the regex pattern 
    if re.match(email_regex, email):
        return True
    else:
        return False
    
def validate_phone_number(phone_number):
    #this is regex pattern to allow numbers, spaces, +, _, and parentheses
    pattern = r'^\+?[0-9\s\-()]{7,15}$'

    #validate phone number
    if re.match(pattern, phone_number):
        return True
    else:
        print("Invalid phone number. Please enter a 10-digit number, e.g., 123-456-7890.")
        return False
def validate_sector(company_sector):
    if company_sector.lower() in [sector.lower() for sector in valid_sectors]:
        return True
    else:
        print("Company sector is not listed")
        print("Here are the available company sectors you can search:")
        print("Finance")
        print("Technology")
        print("Real Estate")
        return False
def validate_source(lead_source):
    if lead_source.lower() in [source.lower() for source in valid_lead_sources]:
        return True
    else:
        print("Lead source is not listed")
        return False
def validate_date(date_created):
    """This is a function to validate if an input date is in the correct format

    Returns True if valid, False otherwise
    """
    try:
        #try to parse the input date using the format 'yyyy/mm/dd'
        datetime.strptime(date_created, "%Y/%m/%d")
        return True
    except ValueError:
        print("Invalid date. Please enter a date in the format 'yyyy/mm/dd'.")
        return False
def validate_sales(sales_rep):
    if sales_rep.lower() in [rep.lower() for rep in valid_sales_reps]:
        return True
    else:
        print("Sales representation is not listed")
        return False
def filter_leads_by_month(month):
    """Function to filter and sum transactions for a given month."""
    
    # Normalize the input to lowercase to make it case-insensitive
    month = month.lower()
    
    if month in months_map:
        month_number = months_map[month]
        total_transaction_value = 0
        filtered_leads = []

        # Loop through the leads data and filter by the given month
        for lead in data_lead:
            lead_date = lead["date_created"]
            lead_month = lead_date.split("-")[1]  # Extract the month from the 'date_created' field
            
            if lead_month == month_number:
                filtered_leads.append(lead)
                total_transaction_value += lead.get("Transaction", 0)  # Use .get() to avoid KeyError

        # Check if any leads were found
        if filtered_leads:
            print(f"Total transaction value in {month.capitalize()}: {total_transaction_value}")
        else:
            print(f"No leads found for {month.capitalize()}.")
    else:
        print("Invalid month name. Please enter a valid month.")
def generate_summary_report(data_leads):
    """Generate a summary report of leads by company sector."""
    report = defaultdict(int)  # Use defaultdict to avoid key errors

    for lead in data_leads:
        sector = lead['company_sector']
        report[sector] += 1  # Increment the count for each sector

    return report
def export_to_csv(data_leads, filename):
    """Export leads data to a CSV file."""
    fieldnames = data_leads[0].keys()  # Extract column headers from the first dictionary

    with open(f"{filename}.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(data_leads)  # Write all the rows of lead data

    print(f"Data successfully exported to {filename}.csv")

def export_to_excel(data_leads, filename):
    """Export leads data to an Excel file using pandas."""
    df = pd.DataFrame(data_leads)  # Convert the list of dictionaries to a pandas DataFrame
    df.to_excel(f"{filename}.xlsx", index=False)  # Export to Excel without including the index

    print(f"Data successfully exported to {filename}.xlsx")

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
            elif menu_choice == 2:
                create_data_lead()  # Ensure this function is defined
            elif menu_choice == 3:
                update_data_lead()  # Ensure this function is defined
            elif menu_choice == 4:
                delete_data()  # Ensure this function is defined
            elif menu_choice == 5:
                transaction()
            elif menu_choice == 6:
                report_menu(data_lead)
            elif menu_choice == 7:
                print("Exiting program, Goodbye!")
                exit()  # Break the outer loop and exit the program
            else:
                print("Invalid choice. Please select a valid option.")


        
    else:
        # Failed login, retry
        print("Login failed. Please try again.")
        