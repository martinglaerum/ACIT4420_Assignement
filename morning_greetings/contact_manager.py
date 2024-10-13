import os

    # Absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# contacts_manager.py
class ContactsManager:
    contacts = []
    def __init__(self):
        contacts = []
            # Finds the current file path of the file containing the contacts
        file_path = os.path.join(BASE_DIR, "contacts.txt")

            # Opens and reads all contacts stored in the contacts.txt file
        with open(file_path, 'rt') as f:
            for line in f:
                name, email, preferred_time = line.strip().split(',')
                self.contacts.append({
                    'name': name,
                    'email': email,
                    'preferred_time': preferred_time
                })

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        self.contacts.append({
                    'name': name,
                    'email': email,
                    'preferred_time': preferred_time
                })
        self.save_contacts()

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_contacts()

    def get_contacts(self):
        return self.contacts

        # Writes changes to the contacts to the contact.txt file
    def save(self):
        file_path = os.path.join(BASE_DIR, "contacts.txt")

        with open(file_path, 'wt') as file:
            for contact in self.contacts:
                # Formatting each contact dictionary as a line
                file.write(f"{contact['name']},{contact['email']},{contact['preferred_time']}\n")

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")


def manage():
        # Creates an object containing all contacts
    Contacts = ContactsManager()

    print("What do you want to do")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. List all contacts")
    choice = input("Enter the representing your choice: ")

    if choice == '1':
        name = input("Name of the new contact: ")
        email = input(f"{name}'s email: ")
        preferred_time = input(f"{name}'s preffered time to be contacted: ")
        Contacts.add(name, email, preferred_time)
    elif choice == '2':
        name = input("Name of the contact to remove: ")
        Contacts.remove(name)
    elif choice == '3':
        Contacts.list_contacts()
    else:
        print("Invalid choice. Please choose a valid number.")