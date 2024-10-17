import subprocess
import platform
import smtplib
import random
from src.banner import display_banner
from src.core import load_email_credentials, load_receiver_email, load_email_body, send_emails, load_email_subject
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Clear the screen function
def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

# Function to show the main menu
def show_menu(error_message=""):
    clear_screen()  # Clear the screen before showing the banner
    display_banner()  # Display the banner each time
    print(f"{Fore.BLUE}MENU:{Style.RESET_ALL}")  # Menu header in blue
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} AUTOMATIC SENDING (1ST NUMBER BY 1ST EMAIL){Style.RESET_ALL}")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} MANUAL SENDING (CHOOSE EMAIL){Style.RESET_ALL}")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} EXIT{Style.RESET_ALL}")

    # Show error message if provided
    if error_message:
        print(f"{Fore.RED}{error_message}{Style.RESET_ALL}")

# Function to load names (example list, you can change or load it from a file if needed)
def load_names():
    return ["Alice", "Bob", "Charlie", "David", "Eve"]

# Automatic Sending Function
def automatic_sending():
    phone_numbers = input(f"{Fore.GREEN}Enter the phone numbers (separated by commas): {Style.RESET_ALL}").split(',')
    phone_numbers = [number.strip() for number in phone_numbers]
    
    # Load names for the random name generation
    names = load_names()

    # Send emails with the provided phone numbers
    send_emails(sender_emails, receiver_email, email_body_template, names, phone_numbers)

    # Wait for user input before returning to the main menu
    input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")

# Manual Sending Function
def manual_sending():
    # Load names for the random name generation
    names = load_names()

    while True:
        clear_screen()  # Clear the screen before showing the banner
        display_banner()  # Display the banner
        print(f"{Fore.BLUE}CHOOSE AN EMAIL:{Style.RESET_ALL}")
        for index, sender in enumerate(sender_emails):
            print(f"{Fore.GREEN}{index + 1}.{Style.RESET_ALL} {sender['email']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}0.{Style.RESET_ALL} BACK TO MAIN MENU{Style.RESET_ALL}")

        email_choice = input(f"{Fore.GREEN}Enter the number of the email you want to use: {Style.RESET_ALL}")

        if email_choice.isdigit() and 1 <= int(email_choice) <= len(sender_emails):
            selected_sender = sender_emails[int(email_choice) - 1]  # Get the selected email
            phone_number = input(f"{Fore.GREEN}Enter the phone number to send: {Style.RESET_ALL}")

            # Format the body with the phone number and a random name
            random_name = random.choice(names)
            message_body = email_body_template.format(phone_number, random_name)

            # Get the subject, defaulting to a space if SUBJECT.txt is empty
            subject = load_email_subject("SUBJECT.txt")
            subject = subject if subject.strip() else " "  # Default subject is a single space

            # Create the full email text
            email_text = f"Subject: {subject}\n\n{message_body}"

            # Sending the email
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(selected_sender["email"], selected_sender["password"])
                server.sendmail(selected_sender["email"], receiver_email, email_text)
                print(f"EMAIL SENT FROM {Fore.GREEN}{selected_sender['email']}{Style.RESET_ALL} TO {Fore.BLUE}{receiver_email}{Style.RESET_ALL} WITH PHONE NUMBER {Fore.YELLOW}{phone_number}{Style.RESET_ALL}")
            except Exception as e:
                print(f"Error sending email from {selected_sender['email']}: {e}")
            finally:
                server.quit()

            # Wait for user input before returning to the main menu
            input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")
        elif email_choice == '0':
            break  # Go back to the main menu
        else:
            print(f"{Fore.RED}Invalid email choice. Please try again.{Style.RESET_ALL}")
            input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")  # Wait for user to acknowledge

# Load email and password from SENDER.txt file
sender_emails = load_email_credentials("SENDER.txt")
receiver_email = load_receiver_email("RECIEVER.txt")
email_body_template = load_email_body("BODY.txt")

# If no credentials were loaded or receiver email is None, exit
if not sender_emails or receiver_email is None or email_body_template is None:
    print("No valid email credentials or receiver email or email body found. Exiting...")
    exit()

# Main Loop
while True:
    show_menu()  # Show the menu without an error message
    
    user_choice = input(f"{Fore.GREEN}Choose an option{Style.RESET_ALL} (1-3): ")

    if user_choice == '1':
        automatic_sending()
    elif user_choice == '2':
        manual_sending()
    elif user_choice == '3':
        print("Exiting the program.")
        break
    else:
        # Instead of clearing the screen, show the menu with the error message
        show_menu("Invalid option. Please try again.")  # Show the menu again with the error message
        input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")  # Wait for user to acknowledge
