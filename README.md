# ACIT4420_Message_Sender

**ACIT4420_Message_Sender** is a tool for that will automatically create and send morning greeting messages to a specified list of contacts. The package includes the functionality of creating and managing a list of contacts. This list contains names, emails and preffered time to be messaged. The package also contains the ability to create, send and log messages.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Games Included](#games-included)
- [Project Structure](#project-structure)
- [License](#license)
## Features
- Automatically sends personalized morning greeting messages
- Messages are sent using a manageable list of contacts
- Logs all messages sent
- Functional code containing error handling
- Easy to install and run using a command-line interface
## Installation
To get started, follow these steps:
1. **Clone the Repository** (or download the package):
   ```bash
   git clone https://github.com/martinglaerum/ACIT4420_Message_Sender.git
   cd ACIT4420_Message_Sender
   ```
2. **Create a Virtual Environment** (recommended):
   ```bash
   python3 -m venv gameenv
   source gameenv/bin/activate  # On Windows, use `gameenv\Scripts\activate`
   ```
3. **Install the Package**:
   ```bash
   pip install -e .
   ```
## Usage
Once installed, you can use the tool by running the following command in your terminal:
```bash
morning_greetings
```
This will launch a menu where you can choose one of the following
1. **Send messages**
2. **Manage contacts**
Choosing **Send messages** will automatically send the personalized messages to all the contacts. Choosing **Manage contacts** will allow you to add or remove contacts.
## Project Structure
Here is a brief overview of the project's structure:
```
ACIT4420_Message_Sender/
│
├── morning_greetings/
│   ├── __init__.py
│   ├── main.py                # Entry point for the game menu
│   ├── contact_manager.py
│   ├── contacts.txt
│   ├── message_generator.py 
│   ├── message_sender.py 
│   ├── logger.py 
│   └── message_log.txt
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files:
- **`main.py`**: Contains the main function that launches the game menu.
- **`setup.py`**: Script for installing the package.
- **`contact_manager.py`**: Script for managing the contacts.
- **`message_generator.py `**: Script creating a personalized message.
- **`message_sender.py`**: Script for sending a message.
- **`logger.py`**: Script for logging information about sent messages.

