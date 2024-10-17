import smtplib
import os
import re
import random
from colorama import Fore, Style  # Import Fore and Style from colorama

# Function to read email and password from file
def load_email_credentials(file_name):
    credentials = []
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"{file_name} not found in the current directory.")
        
        with open(file_name, 'r') as file:
            for line in file:
                # Use regex to match the format "email"@"password" including spaces
                match = re.match(r'"([^"]+)"@"([^"]+)"', line.strip())
                if match:
                    email, password = match.groups()
                    credentials.append({"email": email, "password": password})
                else:
                    raise ValueError("File format is incorrect. Each line should be '\"email\"@\"password\"'.")
    except Exception as e:
        print(f"Error loading email credentials: {e}")
    return credentials

# Function to read the receiver email from file
def load_receiver_email(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"{file_name} not found in the current directory.")
        
        with open(file_name, 'r') as file:
            line = file.readline().strip()
            if line:
                return line
            else:
                raise ValueError("Receiver email file is empty.")
    except Exception as e:
        print(f"Error loading receiver email: {e}")
        return None

# Function to read the email body from file
def load_email_body(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"{file_name} not found in the current directory.")
        
        with open(file_name, 'r') as file:
            body = file.read().strip()
            if body:
                return body
            else:
                raise ValueError("Email body file is empty.")
    except Exception as e:
        print(f"Error loading email body: {e}")
        return None

# Function to load the email subject from file
def load_email_subject(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"{file_name} not found in the current directory.")
        
        with open(file_name, 'r') as file:
            subject = file.read().strip()
            if subject:
                return subject
            else:
                return " "  # Default subject as a space if the file is empty
    except Exception as e:
        print(f"Error loading subject: {e}")
        return " "  # Default subject as a space if there is an error

# Function to send emails
def send_emails(sender_emails, receiver_email, email_body_template, names, phone_numbers):
    subject = load_email_subject("SUBJECT.txt")  # Load subject from file or use default

    # Check if we have enough email accounts for the numbers
    if len(phone_numbers) > len(sender_emails):
        print("Error: You don't have enough email accounts for the number of phone numbers.")
        return

    # Sending an email for each phone number using a different sender email
    for i, phone_number in enumerate(phone_numbers):
        sender = sender_emails[i]  # Get the corresponding sender email and password
        sender_email = sender["email"]
        sender_password = sender["password"]

        # Generate a random name for each email
        random_name = random.choice(names)
        
        # Replace placeholders in the email body
        message_body = email_body_template.format(phone_number, random_name)
        email_text = f"Subject: {subject}\n\n{message_body}"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, email_text)
            print(f"EMAIL SENT FROM {Fore.GREEN}{sender_email}{Style.RESET_ALL} TO {Fore.BLUE}{receiver_email}{Style.RESET_ALL} WITH PHONE NUMBER {Fore.YELLOW}{phone_number}{Style.RESET_ALL}")
        except Exception as e:
            print(f"Error sending email from {sender_email}: {e}")
        finally:
            server.quit()
