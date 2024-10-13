def send_message(email, message):
        # Checks that there is a email specified
    if not email:
        raise ValueError("Email address is missing")
        # Simulate sending a message (replace this with actual email sending logic if needed)
    
        # Sending the message
    print(f"Sending message to {email}: {message}")