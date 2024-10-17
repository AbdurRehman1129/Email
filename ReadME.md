
---

## Email Sending Automation Script

This Python script automates sending emails to multiple recipients. It allows you to automatically or manually select sender emails, send customized messages with dynamic placeholders (like phone numbers and names), and handle multiple email accounts efficiently. Ideal for bulk messaging where each message needs some personalized information.

### Features:
- **Automatic Sending**: Automatically send emails using pre-configured sender emails and dynamic recipient details.
- **Manual Sending**: Choose which sender email to use for each email manually.
- **Dynamic Email Content**: Customize emails with placeholders for phone numbers and names, allowing personalized emails to be sent in bulk.
- **Error Handling**: Properly handles and logs errors encountered during sending.

---

## Installation

### For Termux:

1. **Update and install dependencies:**
   Update package lists and upgrade existing packages. Install Python and Git.

   ```bash
   apt update && apt upgrade
   ```

   ```bash
   pkg install python
   ```

   ```bash
   pkg install git
   ```

2. **Clone the repository:**
   Download the repository from Codeberg and navigate into the cloned directory.

   ```bash
   git clone https://codeberg.org/AbdurRehman1/Email.git
   ```

   ```bash
   cd Email
   ```

3. **Install required Python libraries:**
   Install all necessary Python libraries listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Edit the sender details:**
   Open `SENDER.txt` to input or modify the sender email details.

   ```bash
   nano SENDER.txt
   ```

5. **Edit the email body (optional):**
   Open `BODY.txt` to customize the content of the email body.

   ```bash
   nano BODY.txt
   ```

6. **Edit the email subject (optional):**
   Open `SUBJECT.txt` to specify or modify the email subject line.

   ```bash
   nano SUBJECT.txt
   ```

7. **Edit the receiver email:**
   Open `RECIEVER.txt` to add or change the receiver's email address.

   ```bash
   nano RECIEVER.txt
   ```

8. **Run the script:**
   Execute the main Python script to start sending emails.

   ```bash
   python main.py
   ```

---

### For Windows:

1. **Install Python and Git:**  
   Download and install [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/download/win) if not already installed.

2. **Clone the repository:**
   Open Command Prompt and download the repository from Codeberg.

   ```cmd
   git clone https://codeberg.org/AbdurRehman1/Email.git
   ```

   ```cmd
   cd Email
   ```

3. **Install required Python libraries:**
   Install the Python libraries specified in the `requirements.txt` file.

   ```cmd
   pip install -r requirements.txt
   ```

4. **Edit the sender details:**
   Open `SENDER.txt` with Notepad to input or modify sender email details.

   ```cmd
   notepad SENDER.txt
   ```

5. **Edit the email body (optional):**
   Open `BODY.txt` with Notepad to customize the content of the email body.

   ```cmd
   notepad BODY.txt
   ```

6. **Edit the email subject (optional):**
   Open `SUBJECT.txt` with Notepad to specify or modify the email subject line.

   ```cmd
   notepad SUBJECT.txt
   ```

7. **Edit the receiver email:**
   Open `RECIEVER.txt` with Notepad to add or change the receiver's email address.

   ```cmd
   notepad RECIEVER.txt
   ```

8. **Run the script:**
   Execute the main Python script to start sending emails.

   ```cmd
   python main.py
   ```

---

