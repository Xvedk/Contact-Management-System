contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    gender = input("Enter gender (Male/Female/Other): ")
    contacts[name] = {
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "gender": gender
    }
    print(f"{name} added to contacts.")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone_number']}, Gender: {contact_info['gender']}")
def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone_number']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for name, contact_info in contacts.items():
        if query in (name, contact_info['phone_number']):
            print(f"Name: {name}, Phone: {contact_info['phone_number']}, Email: {contact_info['email']}, Address: {contact_info['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address,
        }
        print(f"{name}'s contact information updated.")
    else:
        print(f"Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted from contacts.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. View Contact Details")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            view_contact_details()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_contact_details():
    name = input("Enter the name of the contact to view details: ")
    if name in contacts:
        contact_info = contacts[name]
        print("Contact Details:")
        print(f"Name: {name}")
        print(f"Phone: {contact_info['phone_number']}")
        print(f"Email: {contact_info['email']}")
        print(f"Address: {contact_info['address']}")
        print(f"Gender: {contact_info['gender']}")
    else:
        print("Contact not found.")

if __name__ == "__main__":
    main()
