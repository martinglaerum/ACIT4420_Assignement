def send_message(email, message):

        # Checks that there is an email specified
    if not email:
        raise ValueError("Email address is missing")
    
        # Sends the message
    print(f"Sending message to {email}: {message}")
