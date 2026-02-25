# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # create new contact and populate it with the given information
    new_contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "category": category,  # friend, family, work, other
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S") # using current time as marker for creation date
    }
    contacts.append(new_contact)
    return new_contact


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    print("=" * 44)
    print(f"    CONTACT BOOK ({len(contacts)} contacts)")
    print("=" * 44)
    print("#  | Name            | Phone         | Category")
    print("---|-----------------|---------------|----------")
    c_no = 1 # used to keep count of which contact # it is in the list
    for contact in contacts: # loop through contacts list and print all in a certain format
        print(f"{c_no}  | {contact["name"]} | {contact["phone"]} | {contact["category"]}")
        c_no+=1


def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    print("--- Contact Details ---")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    print(f"Email: {contact["email"]}")
    print(f"Category: {contact["category"]}")
    print(f"Added: {contact["created_at"]}")


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # Hint: Use list comprehension and .lower()
    matches_found = []
    for contact in contacts: # loop through and find matches
        name = contact["name"]
        if query.lower() in name.lower(): # check if any substring contains query string
            matches_found.append(contact)
    return matches_found


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    matches_found = []
    for contact in contacts:
        cat = contact["category"] # category of current contact in loop
        if cat == category:
            matches_found.append(contact)
    return matches_found


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    matches_found = []
    for contact in contacts:
        contact_number = contact["phone"] # phone # of current contact in loop
        if contact_number == phone:
            matches_found.append(contact)
    return matches_found


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    for contact in contacts:
        contact_phone = contact["phone"]
        if contact_phone == phone: # found!
            if field.lower() not in ["name", "phone", "email", "category"]:
                print(f"ERROR, no such field as {field}")
                return False
            contact[field.lower()] = new_value
            return True
    print("Contact not found...")
    return False # contact not found


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    for i in range(len(contacts)): # need the index for deletion later
        contact_phone = contacts[i]["phone"]
        if contact_phone == phone: # found target
            print(f"deleting {contacts[i]["name"]} from contacts list...")
            contacts.pop(i)
            return True
    print("contact not found...")
    return False # not found



# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """

    # doing calculations for stats
    total_contacts = len(contacts)
    family = 0
    work = 0
    other = 0
    for contact in contacts: # loop through and tally categories
        category = contact["category"]
        if category.lower() == "family":
            family += 1
        elif category.lower() == "work":
            work += 1
        else:
            other += 1

    # printing stats
    print("--- Contact Book Statistics ---")
    print(f"TOTAL CONTACTS: {total_contacts}")
    print("By Category:")
    print(f"    -Family: {family}")
    print(f"    -Work: {work}")
    print(f"    -Other: {other}")

# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    display_menu()
    user_input = input("Enter Command >")
    while True:
        if user_input in ["0","1","2","3","4","5","6"]:
            user_input = int(user_input)
            if user_input == 0:
                print("Shutting down...")
                exit(0)
            elif user_input == 1: # START OF COMMAND 1===========================
                print("printing contact list...")
                display_all_contacts(contacts)
            elif user_input == 2:# START OF COMMAND 2===========================
                name = input("Contact name: ")
                phone = input("Phone Number: ")
                email = input("email: ")
                category = input("What Category are they: ")
                temp = add_contact(contacts,name, phone, email, category)
                print(f"Contact successfully added... {temp}")
            elif user_input == 3:# START OF COMMAND 3===========================
                choice = int(input("What method do you want? 1:name, 2:category, 3:phone"))
                if choice == 1:
                    name = input("What is their name?: ")
                    print(search_by_name(contacts, name))
                elif choice == 2:
                    category = input("What category are they in?: ")
                    print(filter_by_category(contacts, category))
                elif(choice == 3):
                    phone = input("What is their phone Number?: ")
                    print(find_by_phone(contacts, phone))
                else:
                    print("Error, invalid selection try again...")
            elif user_input == 4: # START OF COMMAND 4===========================
                phone = input("whats their phone?: ")
                field = input("field to update(name, email, phone#, category):")
                new_value = input("what do i change it to?: ")
                if update_contact(contacts, phone, field, new_value):
                    print("Successfully changed contact information!")
                else:
                    print("Failure to change contact info...")
            elif user_input == 5:
                phone = input("whats their phone?: ")
                if delete_contact(contacts, phone):
                    print("Successfully deleted contact from contact book")
                else:
                    print("Failure to delete contact from contact book...")
            elif user_input == 6:
                display_statistics(contacts)


        else:
            print("Command not recognized, please try again...")
        display_menu()
        user_input = input("Enter Command >")




# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    contacts = []
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Bob Builder", "123-456-7890", "bob@example.com", "work")
    add_contact(contacts, "Cat", "322-223-2211", "cat@example.com", "family")
    add_contact(contacts, "Dog", "322-223-2212", "dog@example.com", "family")
    add_contact(contacts, "Emmet", "777-209-9012", "emmet@example.com", "friend")

    main()
