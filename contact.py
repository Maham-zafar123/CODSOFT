import os


def welcome_msg():
    print("\n\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ WELCOME TO MY CONTACT MANAGER ☆*: .｡. o(≧▽≦)o .｡.:*☆\n")


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("\n\t\t\tNo contacts to display.")
        else:
            print("\n\t\t\tContacts:")
            for contact in self.contacts:
                self.print_contact_info(contact)

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                found_contacts.append(contact)

        if not found_contacts:
            print("\n\t\t\tNo matching contacts found.")
        else:
            print("\n\t\t\tSearch Results:\n")
            for contact in found_contacts:
                self.print_contact_info(contact)

    def update_contact(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                contact.address = address
                return

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return

    def print_contact_info(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")
        print("")

    def save_contacts_to_file(self, file_path):
        try:
            sorted_contacts = sorted(
                self.contacts, key=lambda x: x.name.lower())
            with open(file_path, 'w') as file:
                for contact in sorted_contacts:
                    file.write(
                        f"{contact.name},{contact.phone},{contact.email},{contact.address}\n")
            print("\n\t\t\tContacts saved to file successfully!\n")
        except Exception as e:
            print(
                f"\n\t\t\tAn error occurred while saving contacts: {str(e)}\n")

    def load_contacts_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, phone, email, address = line.strip().split(',')
                    self.add_contact(name, phone, email, address)
            print("\n\t\t\tContacts loaded from file successfully!\n")
        except FileNotFoundError:
            print("\n\t\t\tFile not found.\n")
        except Exception as e:
            print(
                f"\n\t\t\tAn error occurred while loading contacts: {str(e)}\n")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nHERE THE CONTACT MANAGER MENU: \n\n")
        print("\t\t→ Press 1 to Add Contact")
        print("\t\t→ Press 2 to View Contacts")
        print("\t\t→ Press 3 to Search Contact")
        print("\t\t→ Press 4 to Update Contact")
        print("\t\t→ Press 5 to Delete Contact")
        print("\t\t→ Press 6 to Save Contacts to File")
        print("\t\t→ Press 7 to Load Contacts from File")
        print("\t\t→ Press 8 to Exit\n\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of person: ")
            phone = input(f"Enter phone number of {name} : ")
            email = input(f"Enter email of {name} : ")
            address = input(f"Enter address of {name} : ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            phone = input(f"Enter new phone number of {name} : ")
            email = input(f"Enter new email of {name} : ")
            address = input(f"Enter new address of {name} : ")
            contact_manager.update_contact(name, phone, email, address)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            file_path = input(
                "Enter the path to save contacts to (e.g., contacts.txt): ")
            contact_manager.save_contacts_to_file(file_path)
        elif choice == "7":
            file_path = input(
                "Enter the path to load contacts from (e.g., contacts.txt): ")
            contact_manager.load_contacts_from_file(file_path)
        elif choice == "8":
            print("\n\t\t\tExiting Contact Manager.\n")
            break
        else:
            print("\n\t\t\tInvalid choice. Please try again.\n")


if __name__ == "__main__":
    welcome_msg()
    main()
