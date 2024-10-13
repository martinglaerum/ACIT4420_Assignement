import os

    # Absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ContactsManager:
    '''Manages a list of contacts stored in a text file.'''

        # Dictionary containing the contacts
    contacts = []
  
    def __init__(self):
        '''Initializes the contacts dictionary'''
        self.contacts = []
            # Finds the current file path for the file containing the contacts
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
        '''Adds a new contact to the contacts dictionary'''
        self.contacts.append({
                    'name': name,
                    'email': email,
                    'preferred_time': preferred_time
                })
        
            # Saves the new contact to the contacts.txt file
        self.save_contacts()

        
    def remove_contact(self, name): 
        '''Removes a contact if the inputted name matches an existing contact'''
        self.contacts = [c for c in self.contacts if c['name'] != name]

            # Saves the new contact to the contacts.txt file
        self.save_contacts()

        
    def get_contacts(self):
        '''Returns the contacts dictionary'''
        return self.contacts

        
    def save_contacts(self):
        '''Saves changes in the contacts dictionary to the contact.txt file'''

            # Finds the file path to the contacts.txt file
        file_path = os.path.join(BASE_DIR, "contacts.txt")

            # Writes the contacts dictionary to the contacts.txt file
        with open(file_path, 'wt') as file:
            for contact in self.contacts:
                    # Formats each contact as a line with specific syntax so the file can easily be read
                file.write(f"{contact['name']},{contact['email']},{contact['preferred_time']}\n")

        
    def list_contacts(self):
        '''Lists all the contacts in the contacts dictionary'''
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")


def manage():
    '''Provides a command-line interface for managing contacts.'''

        # Creates an object containing all contacts
    contacts = ContactsManager()

    print("What do you want to do")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. List all contacts")
    choice = input("Enter the representing your choice: ")

        
    if choice == '1': # Creates a new contact
        name = input("Name of the new contact: ")
        email = input(f"{name}'s email: ")
        preferred_time = input(f"{name}'s preffered time to be contacted: ")
        contacts.add_contact(name, email, preferred_time)
    elif choice == '2':  # Removes a contact
        name = input("Name of the contact to remove: ")
        contacts.remove_contact(name)
    elif choice == '3': # Lists all contacts
        contacts.list_contacts()
    else:
        print("Invalid choice. Please choose a valid number.")
