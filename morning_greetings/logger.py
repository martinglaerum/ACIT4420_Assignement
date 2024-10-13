import os
import datetime

    # Finds the absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log_message(contact, message):
    '''Logs all messages sent into a seperate file'''
    file_path = os.path.join(BASE_DIR, "message_log.txt") # Specifies the path to the log file

        # Opens the log file and stores the message sent, including who it was sent to and when it was sent
    with open(file_path, "at") as f:
        f.write(f"Time: {datetime.datetime.now()}, The following message was sent to {contact}: {message}\n")
