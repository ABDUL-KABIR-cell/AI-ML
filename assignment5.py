def save_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name} - {phone}\n")
    print("Contact saved!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                print("\nSaved Contacts:")
                for contact in contacts:
                    print(contact.strip())
    except FileNotFoundError:
        print("No contacts saved yet.")

def main():
    while True:
        print("\nSimple Contact Saver")
        print("1. Save Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            save_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
