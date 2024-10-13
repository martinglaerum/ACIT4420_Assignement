import sys
import os

    # Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import contact_manager
import message_generator
import message_sender
import logger



def main():
    print("What do you want to do:")
    print("1. Send messages")
    print("2. Manage contacts")
    choice = input("Enter the representing your choice: ")

    if choice == '1': # Sends messages to all contacts in the contacts.txt file

        contacts = contact_manager.ContactsManager() # Creates an object containing the contacts
           
            # Sends a message for each contact
        for people in Contacts.contacts:
            try:
                message = message_generator.generate_message(people["name"]) # Creates the message
                message_sender.send_message(people["email"], message) # Sends the message
                logger.log_message(people["name"], message) # Logs the message
            except Exception as e:
                print(f"Error sending message to {people['name']}: {e}")
    elif choice == '2':
        contact_manager.manage() # Calls the function that manages the contacts
    else:
        print("Invalid choice. Please choose a valid number.")

if __name__ == "__main__":
    main()
