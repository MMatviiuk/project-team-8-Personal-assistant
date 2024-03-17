# Address Book Assistant Bot (Terminal Personal Assistant)

This Python program functions as a user-friendly terminal-based personal assistant specifically designed to manage your contacts. It empowers you to effortlessly add, view, edit, and delete contact information, keeping your address book organized and accessible.

## Features

Comprehensive Contact Management: Create, store, update, and remove contact entries.
Detailed Information: Manage phone numbers, birthdays, emails, addresses, and even add personalized notes.
Intuitive Command System: Interact with the assistant using clear and concise commands.
User-Friendly Output: Receive clear messages and formatted contact information.
Error Handling: Gracefully handle incorrect or missing commands, providing helpful feedback.

## Installation

1. Prerequisites: Ensure you have Python 3.x installed on your system. Verify by running python3 --version in your terminal.

2. Dependencies: The program relies on certain external libraries. Install them using pip:

```bash
pip install -r requirements.txt
```

Run the Program: Execute the main Python script (e.g., main.py) using the command prompt or terminal:

```bash
pip install -e . 
```


## Usage
Run the Program: Execute the main Python script (e.g., main.py) using the command prompt or terminal:

```Bash
termminal
```


## Interact with the Assistant: 

You'll be greeted by "Welcome to the assistant bot!". Type a command and press Enter. Here are some examples:

* `add John 1234567890` : Create a new contact named "John Doe" with phone number "123-456-7890".
* `phone John` : Display the phone number of "John Doe".
* `change-birthday` : John Doe 2000-01-01: Update the birthday of "John Doe" to "2000-01-01".
* `add-email John johndoe@example.com` : Add an email address "johndoe@example.com" to "John Doe".
* `show-address Jane` : View the address of "Jane Smith".
* `add-note` : This is a reminder for John Doe.: Add a note associated with "John Doe".
* `show-notes` : Display all notes.
* `help` : Display a list of available commands.
* `exit` : Terminate the program.

## Explanation of Commands

A detailed list of available commands will be provided within the program itself (using the help command) or documented elsewhere (consider creating a separate commands.md file for a more comprehensive list).

Data Storage (Optional)

The program can load and save data to a persistent storage mechanism like JSON files or a database (depending on your implementation). This ensures that your contact information is preserved even if you exit the program.

## Additional Considerations

Customization: You can extend the program's functionality to handle more complex tasks, such as searching contacts by various criteria, generating birthday reminders, or integrating with other personal management tools.
Security: If you plan to store sensitive information, explore secure data storage and encryption techniques.

### Contribution

If you're interested in contributing to this project, feel free to fork the repository on GitHub (if applicable) and submit pull requests with your enhancements.

### Disclaimer

This README.md provides a general overview. The specific functionality and behavior may vary depending on the actual implementation of the program. For detailed usage instructions, refer to the provided commands within the program or any additional documentation.
