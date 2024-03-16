from .classes import Record, Birthday, AddressBook, Email, Phone, Note, Note
from .check import *
from .classes import Record
from .validate import email_is_valid

from datetime import datetime
from collections import defaultdict
from re import fullmatch




def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Wrong format. Use 'help' for additional imformation."
            #return f"Error: {e}"
        except KeyError:
            return "Wrong format. Use 'help' for additional imformation."
            #return "Please provide a name."
        except IndexError as e:
            return "Wrong format. Use 'help' for additional imformation."
            #return f"Error: {e}"
        except NameError as e:
            return "Wrong format. Use 'help' for additional imformation."
            #return f"Error: {e}"
        except TypeError as e:
            return "Wrong format. Use 'help' for additional imformation."
            #return f"Error: {e}"
            
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Phone -----------------------------------------------------------------------------
@input_error
def add_contact(args, book):
    """
    Function to add a new contact.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the addition result.
    """
    name, phone = args
    if len(phone) != 10 or not phone.isdigit():
        return "Error: Invalid phone number format. Please enter a 10-digit number."
    record = Record(name)
    record.add_phone(phone)
    book[name] = record
    return "Contact added."


def show_phone(args, book):
    (name,) = args
    if name in book:
        record = book[name]

        res = []
        for phone in record.phones:
            res.append(phone.value)
        return f"{name}: {','.join(res)}"
    else:
        return "Sorry, {name} isn't exist. Use 'add' for append this contact."


@input_error
def change_contact(args, book):
    """
    Function to change an existing contact.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the change result.
    """
    name, field, new_value = args
    if name in book:
        record = book[name]
        if field == "phone":
            record.phones = [Phone(new_value)]
        elif field == "birthday":
            record.birthday = Birthday(new_value)
        elif field == "email":
            record.emails = [Email(new_value)]
        elif field == "note":
            record.note = new_value
        return f"Contact {name} updated."
    else:
        return f"Sorry, {name} not found."


def get_phones(record):  # Service for get phones from record
    res = []
    for phone in record.phones:
        res.append(phone.value)
    if res[0]:
        return ",".join(res)
    else:
        return "No phone"


# # Find ----------------------------------------------------------------
# @input_error
# def find_contacts(book, field, value):
#     """
#     Function to search for contacts by a given field and value.

#     Args:
#         book: Dictionary with contacts.
#         field: Field to search by (name, phone, birthday, email).
#         value: Value to search for.

#     Returns:
#         List of strings with information about found contacts.
#     """

#     found_contacts_info = []
#     if field == "name":
#         found_contacts = [record for record in book.values() if record.name.lower() == value.lower()]
#     elif field == "phone":
#         found_contacts = [
#             record
#             for record in book.values()
#             if value in [phone.value for phone in record.phones]
#         ]
#     elif field == "birthday":
#         found_contacts = [
#             record
#             for record in book.values()
#             if record.birthday and record.birthday.value.strftime("%d.%m.%Y") == value
#         ]
#     elif field == "email":
#         found_contacts = [
#             record
#             for record in book.values()
#             if value in [email.value for email in record.emails]
#         ]
#     else:
#         found_contacts = []

#     for record in found_contacts:
#         contact_info = f"{record.name}:"
#         contact_info += f"  Phones: {get_phones(record)}"
#         contact_info += f"  Emails: {get_emails(record)}"
#         contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
#         contact_info += f"  Note: {record.note if record.note else 'No note'}"
#         found_contacts_info.append(contact_info)

#     return found_contacts_info


# def show_found_contacts(contacts):
#     """
#     Function to display information about found contacts.

#     Args:
#         contacts: List of found contacts.

#     Returns:
#         String with information about found contacts.
#     """
#     res = []
#     for record in contacts:
#         res.append(f"{record.name}:")
#         res.append(f"  Phones: {get_phones(record)}")
#         res.append(f"  Emails: {get_emails(record)}")
#         res.append(
#             f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
#         )
#         res.append(f"  Note: {record.note if record.note else 'No note'}")
#     return "\n".join(res)


# @input_error
# def find_contact_by_field(args, book):
#     """
#     Function to find a contact by a specified field and value.

#     Args:
#         args: Command line arguments.
#         book: Dictionary with contacts.

#     Returns:
#         String with information about the found contact.
#     """
#     field, value = args
#     found_contacts = find_contacts(book, field, value)
#     if found_contacts:
#         return show_found_contacts(found_contacts)
#     else:
        # return f"No contacts found by {field} with value {value}."


# @input_error
# def change_contact_field(args, book):
#     """
#     Function to change a specified field of a contact.

#     Args:
#         args: Command line arguments.
#         book: Dictionary with contacts.

#     Returns:
#         String with information about the change result.
#     """
#     name, field, new_value = args
#     if name in book:
#         record = book[name]
#         if field == "phone":
#             record.phones = [Phone(new_value)]
#         elif field == "birthday":
#             record.birthday = Birthday(new_value)
#         elif field == "email":
#             record.emails = [Email(new_value)]
#         elif field == "note":
#             record.note = new_value
#         return f"Contact {name} updated."
#     else:
#         return "Sorry, {name} doesn't exist. Use 'add' for append this contact."


@input_error
def show_all(book):
# ============= was table format ==============================================
#     res = []
#     res.append("{:^20}".format("CONTACTS"))
#     res.append("{:^20}".format("-" * 10))
#     for name, record in book.items():
#         res.append("{:<14} {:<14}".format(name + ":", get_phones(record)))
#     res.append("{:^20}".format("=" * 20))
# =============================================================================
    res = ["{:^60}".format("CONTACTS"), "{:-^60}".format("")]
    for name, record in book.items():
        emails = ", ".join(email.value for email in record.emails) or "No Email"
        phones = ", ".join(phone.value for phone in record.phones) or "No Phone"
        birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "No Birthday"
        addresses = "; ".join(f"{address.street}, {address.house_number}, {address.city}, {address.postal_code if address.postal_code else ''}, {address.country if address.country else ''}" for address in record.addresses) or "No Address"
        
        contact_info = f"Name: {name}\nPhone: {phones}\nEmail: {emails}\nBirthday: {birthday}\nAddress: {addresses}\n"
        res.append(contact_info)
        res.append("{:-^60}".format(""))  # Додав розділювач між контактами
    return "\n".join(res)

# Find contact info by name ------------------------------------------------
@input_error
def find(args, book):
    name = args[0]
    if name in book:
        emails = ", ".join(email.value for email in book[name].emails) or "No Email"
        phones = ", ".join(phone.value for phone in book[name].phones) or "No Phone"
        birthday = book[name].birthday.value.strftime('%d.%m.%Y') if book[name].birthday else "No Birthday"
        addresses = "; ".join(f"{address.street}, {address.house_number}, {address.city}, {address.postal_code if address.postal_code else ''}, {address.country if address.country else ''}" for address in book[name].addresses) or "No Address"
        
        contact_info = f"Name: {name}\nPhone: {phones}\nEmail: {emails}\nBirthday: {birthday}\nAddress: {addresses}\n"
        return contact_info
    else:
        return f"Contact {name} not found"

# Birthday ----------------------------------------------------------------
@input_error
def add_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return f"{name}'s birthday added"
    else:
        return f"Sorry, {name} isn't exist. Use 'add' for add this contact."


@input_error
def show_birthday(args, book):
    (name,) = args
    if name in book:
        record = book[name]
        if record.birthday != None:
            birthday = record.birthday.value.strftime("%d.%m.%Y")
            return f"{name}'s birthday is {birthday}"
        else:
            return f"{name}'s birthday isn't recorded"
    else:
        return "Sorry, {name} isn't exist. \nUse 'add' for add this contact to book."

@input_error
def change_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return f"{name}'s birthday changed"
    else:
        return f"Sorry, {name} isn't exist."

@input_error
def delete_birthday(args, book):
    (name,) = args
    if name in book:
        record = book[name]
        if record.birthday != None:
            res = record.remove_birthday()
            return res
        else:
            return f"No birthday for {name}"
    else:
        return "Sorry, {name} isn't exist. \nUse 'add' for add this contact to book."

@input_error
def birthdays(args, book):
    if args:
        days = args[0]
        book.get_birthdays_by_days(days)
    else:
        book.get_birthdays_per_week()


# Email  ----------------------------------------------------------------------
@input_error        
def get_emails(record):
    """
    Function to retrieve emails from a record.

    Args:
        record: Record object.

    Returns:
        String with email addresses.
    """
    res = [email.value for email in record.emails]
    if res:
        return ",".join(res)
    else:
        return "Sorry, {name} doesn't exist. Use 'add' for append this contact."


# "add-email name email": "adding email to existing contact"
@input_error
def add_email(args, book):
    """
    Function to add an email to a contact record.

    Args:
        args (tuple): A tuple containing the name (str) and email (str) to add.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A confirmation message of adding the email.

    Raises:
        ValueError: If the input arguments are not in the correct format.
    """
    name, email = args
    if name in book:
        record = book[name]
        record.emails.append(Email(email))
        return f"{name}'s email added"
    else:
        return f"Sorry, {name} isn't exist. Use 'add' for add this contact."

# "email name": "get email of specific contact"
@input_error
def show_email(args, book):
    """
    Function to get the email of a specific contact.

    Args:
        args (tuple): A tuple containing the name (str) of the contact.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A string containing the contact's name and their email(s).

    Raises:
        ValueError: If the input arguments are not in the correct format.
    """

    name = args[0]

    if name in book:
        record = book[name]
        res = []
        for email in record.emails:
            res.append(email.value)
        return f"{name}: {','.join(res)}"
    else:

        return f"Sorry, {name} isn't exist. Use 'add' for append this contact."

@input_error
def change_email(args, book):
    name = args[0]
    if name in book:
        if book[name].emails:
            for number, email in enumerate(book[name].emails, 1):
                print(f"{number}: {email}")
            while True:
                answer = input("Type the number of email you want to change ===>  ")
                if answer.isdigit() and 1 <= int(answer) <= len(book[name].emails):
                    while True:
                        new_email = input("Enter new email ==>  ")
                        if email_is_valid(new_email):
                            book[name].emails[int(answer)-1] = Email(new_email)
                            return "Email has been changed."
                        else:
                            print("Seems like this email is incorrect. Try again.")
                else:
                    print("Must be the number between 1 and " + str(len(book[name].emails)))
        else:
            return "Contact has no emails."
    else:
        return "No such contact."

# "change-email name email": "changing email of existing contact"
@input_error
def delete_email(args, book):
    """
    Function to delete an email from an existing contact.

    Args:
        args (tuple): A tuple containing the name (str) of the contact and the email (str) to delete.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A confirmation message of deleting the email.

    Raises:
        ValueError: If the input arguments are not in the correct format.
    """
    name, email_to_delete = args
    if name in book:
        record = book[name]
        for email in record.emails:
            if email.value == email_to_delete:
                record.emails.remove(email)
                return f"Email {email_to_delete} deleted from {name}'s contacts."
        return f"Email {email_to_delete} not found in {name}'s contacts."
    else:
        return f"Sorry, {name} isn't exist. Use 'add' for append this contact."


# Address -----------------------------------------------------------------
@input_error
def add_address(args, book):
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.add_address(street, house_number, city, postal_code, country)
        return "Address added."
    else:
        return "Contact does not exist."


@input_error
def show_address(args, book):
    name = args[0]
    if name in book.data:
        record = book.data[name]
        addresses = record.addresses
        if addresses:
            address_str = "\n".join([f"{address}" for address in addresses])
            return f"Addresses for {name}:\n{address_str}"
        else:
            return f"No addresses found for {name}."

    else:
        return "Contact does not exist."


def edit_address(args, book):
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.edit_address(street, house_number, city, postal_code, country)
        return "Address edited."
    else:
        return "Contact does not exist."


def remove_address(args, book):
    (name,) = args
    if name in book.data:
        record = book.data[name]
        record.remove_address()
        return "Address removed."
    else:
        return "Contact does not exist."


# Note --------------------------------------------------------------------


def new_note(notes):
    while True:
        title = input("Type the title here ===>  ")
        if title:
            break
        else:
            print("Title cannot be empty.")
            continue
    text = input("Type the text here ===>  ")
    while True:
        tags = input(
            "Type tags here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
        ).split()
        if all(fullmatch(r"\#\w+", tag) for tag in tags):
            notes.append(Note(title, text, tags))
            return "Note has been added"
        else:
            print("Wrong format.")


def edit_note(notes):
    if notes:
        note = find_note(notes)
        answer = input(
            "Type <y> if you want to change the title or any else key to continue ===>  "
        )
        if answer == "y":
            note.data["title"] = input("Type the new title here ===>  ")
        answer = input(
            "Type <y> if you want to change the text or any else key to continue ===>  "
        )
        if answer == "y":
            note.data["text"] = input("Type the new text here ===>  ")
        answer = input(
            "Type <y> if you want to change tags or any else key to continue ===>  "
        )
        if answer == "y":
            while True:
                tags = input(
                    "Type tags here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
                ).split()
                if all(fullmatch(r"\#\w+", tag) for tag in tags):
                    note.data["tags"] = tags
                    break
                else:
                    print("Wrong format.")
        return "Note has been edited."
    return "No notes added."


def delete_note(notes):
    if notes:
        note = find_note(notes)
        del notes[notes.index(note)]
        return "Note has been deleted."
    return "No notes added."


def find_note(notes):
    note_dict = dict(zip(range(1, len(notes) + 1), notes))
    for number, note in note_dict.items():
        print(str(number) + ": " + note.data["title"])
    while True:
        answer = input("Type the number of note ===>  ")
        if answer.isdigit() and 1 <= int(answer) <= len(notes):
            return notes[int(answer) - 1]
        else:
            print(f"Must be the number between 1 and {len(notes)}")
            continue


def show_notes(notes):
    if notes:
        while True:
            answer = input(
                "What are we looking for? (a for all notes and s for specific) a/s ===>  "
            )
            if answer == "a":
                notes_to_print = notes
                return "\n".join(str(note) for note in notes_to_print)
            elif answer == "s":
                while True:
                    key = input(
                        "What element do you want to search by? (title/text/tags) ===>  "
                    )
                    if key in ("title", "text"):
                        element = input(f"Type the {key} you want to look for ===>  ")
                        notes_to_print = tuple(
                            filter(lambda note: element in note.data[key], notes)
                        )
                        return (
                            "\n".join(str(note) for note in notes_to_print)
                            if notes_to_print
                            else "No such notes."
                        )
                    elif key == "tags":
                        while True:
                            tags = input(
                                "Type the tag(s) you want to look for (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
                            ).split()
                            if all(fullmatch(r"\#\w+", tag) for tag in tags):
                                break
                            else:
                                print("Wrong format.")
                                continue
                        notes_to_print = tuple(
                            filter(
                                lambda note: all(
                                    tag in note.data["tags"] for tag in tags
                                ),
                                notes,
                            )
                        )
                        return (
                            "\n".join(str(note) for note in notes_to_print)
                            if notes_to_print
                            else "No such notes."
                        )
                    else:
                        print("Wrong format.")
                        continue
            else:
                print("Wrong format.")
                continue
    else:
        return "No notes added."


# # Import libraries
#     """
#     The code defines a dictionary of commands with descriptions and numbers, formats the list of
#     commands, and processes user input based on the commands provided.
    
#     :param commands: {
#     :return: The code provided defines two functions: `show_commands(commands)` and
#     `process_input(commands)`.
#     """
# import re

# # Define the commands dictionary
# commands = {
#     # Search
#     "find [name] (1)": "Find contact by name",
#     "phone [name] (2)": "Get person's phone numbers",
#     "email [name] (3)": "Get person's email addresses",
#     "show-birthday [name] (4)": "Get person's birthday",
#     "show-address [name] (5)": "Show person's address",
#     "show-note [name] (6)": "Get person's note",
#     "birthdays (without argument) (7)": "Get all persons with birthdays next week",
#     "birthdays [days] (8)": "Get birthdays list for a custom number of days",
#     "all (9)": "Get all contacts list",

#     # Add
#     "add [name] [phone] (10)": "Add new contact",
#     "add-birthday [name] (11)": "Add person's birthday",
#     "add-email [name] [email] (12)": "Add email to existing contact",
#     "add-address [name] [street] [house_number] [city] [postal_code] [country] (13)": "Add address",
#     "add-note [name] (14)": "Add person's note",

#     # Change
#     "change [name] [phone] (15)": "Change person's phone number",
#     "change-birthday [name] (16)": "Change person's birthday",
#     "edit-address [name] [street] [house_number] [city] [postal_code] [country] (17)": "Edit address",
#     "change-note [name] (18)": "Change person's note",

#     # Delete
#     "delete [name] (19)": "Delete contact",
#     "delete [name] phones (20)": "Delete person's phones",
#     "delete-birthday [name] (21)": "Delete person's birthday",
#     "delete-email [name] [email] (22)": "Delete specific email of a contact",
#     "delete-address [name] (23)": "Delete person's address (by index)",
#     "delete-note [name] (24)": "Delete person's note",
#     "delete [name] notes (25)": "Delete all notes of a contact",

#     # General
#     "help (26)": "Get help",
#     "hello (27)": "Get a greeting",
#     "exit (28)": "Exit the program",
# }

# # Function to format the list of commands
# def show_commands(commands):
#     """
#     This function displays a formatted list of available commands with 
#     descriptions and corresponding numbers for reference.

#     Args:
#         commands: A dictionary where keys are command names (strings) and values 
#                 are descriptions (strings) with command numbers in square brackets.

#     Returns:
#         A string containing the formatted list of commands, separated by newlines.
#     """

#     formatted_commands = []
#     for command, description in commands.items():
#         # Extract the command number within square brackets from the description.
#         command_number = description.split()[-1][1:-1]

#         # Remove the extracted command number from the description for cleaner output.
#         description = ' '.join(description.split()[:-1])

#         # Format the command string with justification and clear separation.
#         formatted_command = f"{command.ljust(36)}({command_number}) ==> {description}"

#         # Add the formatted command string to a list for later joining.
#         formatted_commands.append(formatted_command)

#     # Join all formatted commands with newlines to create the final output string.
#     return "\n".join(formatted_commands)


# # Function to process user input
# def process_input(commands):
#     """
#     This function handles user input, 
#     breaks it down into command and arguments, 
#     and then calls the appropriate function.

#     Args:
#         commands: A dictionary of available commands.

#     Returns:
#         A boolean value indicating whether the program should continue running.
#     """

#     while True:
#         # Get user input
#         user_input = input("Insert command: ").strip().lower()  # Convert input to lowercase and remove whitespace

#         # Exit the program if user enters 'exit'
#         if user_input == "exit":
#             return False

#         # Check if the command is valid
#         if user_input in commands:
#             print(f"Executing command: {user_input}")
#             # Here you would call the appropriate function based on the command and arguments
#         else:
#             print("Invalid command. Please try again.")

# # Call the function to display the commands
# print(show_commands(commands))

# # Call the function to start processing user input
# process_input(commands)

from collections import UserDict
from datetime import datetime, timedelta
import json


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def validate(self):
        if not self.value.isalpha():
            raise ValueError("Name should contain only letters.")


class Phone(Field):
    def validate(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Phone number must be 10 digits and contain only digits.")


class Birthday(Field):
    def validate(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid birthday format. Please use DD.MM.YYYY.")


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.name.validate()
        self.phones = []
        if phones:
            for phone in phones:
                self.add_phone(phone)
        self.birthday = None
        if birthday:
            self.add_birthday(birthday)

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate()
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph

    def add_birthday(self, birthday):
        birthday_obj = Birthday(birthday)
        birthday_obj.validate()
        self.birthday = birthday_obj

    def show_birthday(self):
        return self.birthday.value if self.birthday else "No birthday set"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(str(phone) for phone in self.phones)}, Birthday: {self.show_birthday()}"


class AddressBook(UserDict):
    def __init__(self, filename="address_book.json"):
        self.filename = filename
        self.data = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return {
                    k: Record(v["name"], v["phones"], v["birthday"])
                    for k, v in json.load(f).items()
                }
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name = name.title()
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def show_all(self):
        if self.data:
            for record in self.data.values():
                print(record)
        else:
            print("No contacts found.")

    def get_birthdays_per_week(self):
        today = datetime.today()
        next_week = today + timedelta(days=7)
        birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                if today <= birthday_date <= next_week:
                    birthdays.append((record.name.value, record.birthday.value))
        return birthdays


def main():
    users = [
        {"name": "John", "surname": "Forbes Nash Jr.", "birthday": "13.06.1928"},
        {"name": "Andrew", "surname": "Wiles", "birthday": "11.04.1953"},
        {"name": "Guido", "surname": "van Rossum", "birthday": "31.01.1956"},
        {"name": "Satya", "surname": "Nadella", "birthday": "19.08.1967"},
        {"name": "Demis", "surname": "Hassabis", "birthday": "27.07.1976"},
    ]

    book = AddressBook()

    for user in users:
        name = user["name"]
        phones = []
        birthday = user["birthday"]
        record = Record(name, phones, birthday)
        book.add_record(record)

    commands = {
        "find [name] (1)": "Find contact by name",
        "phone [name] (2)": "Get person's phone numbers",
        "email [name] (3)": "Get person's email addresses",
        "show-birthday [name] (4)": "Get person's birthday",
        "show-address [name] (5)": "Show person's address",
        "show-note [name] (6)": "Get person's note",
        "birthdays (without argument) (7)": "Get all persons with birthdays next week",
        "birthdays [days] (8)": "Get birthdays list for a custom number of days",
        "all (9)": "Get all contacts list",
        "add [name] [phone] (10)": "Add new contact",
        "add-birthday [name] (11)": "Add person's birthday",
        "add-email [name] [email] (12)": "Add email to existing contact",
        "add-address [name] [street] [house_number] [city] [postal_code] [country] (13)": "Add address",
        "add-note [name] (14)": "Add person's note",
        "change [name] [phone] (15)": "Change person's phone number",
        "change-birthday [name] (16)": "Change person's birthday",
        "edit-address [name] [street] [house_number] [city] [postal_code] [country] (17)": "Edit address",
        "change-note [name] (18)": "Change person's note",
        "delete [name] (19)": "Delete contact",
        "delete [name] phones (20)": "Delete person's phones",
        "delete-birthday [name] (21)": "Delete person's birthday",
        "delete-email [name] [email] (22)": "Delete specific email of a contact",
        "delete-address [name] (23)": "Delete person's address (by index)",
        "delete-note [name] (24)": "Delete person's note",
        "delete [name] notes (25)": "Delete all notes of a contact",
        "help (26)": "Get help",
        "hello (27)": "Get a greeting",
        "exit (28)": "Exit the program",
    }

def show_commands():
    """Prints a list of available commands"""
    res = []
    for index, (command, description) in enumerate(commands.items(), start=1):
        res.append(f"  {command:<25} ==> {description} ({index})")  # Use f-strings for cleaner formatting
    return "\n".join(res)

# Simulate the assistant running
print("Welcome to the assistant bot!")
print(show_commands())  # Call the function to display commands

    def process_input(commands):
        while True:
            user_input = input("Enter a command or command number: ").strip()

            if user_input.lower() == "exit":
                print("Good bye!")
                book.save()
                return False

            if user_input.isdigit():
                command_number = int(user_input)
                if 1 <= command_number <= len(commands):
                    command = list(commands.keys())[command_number - 1]
                    print(f"Executing command: {command}")
                    if command == "find [name] (1)":
                        name = input("Enter the name to search for: ")
                        record = book.find(name)
                        if record:
                            print(record)
                        else:
                            print("Contact not found.")
                    elif command == "phone [name] (2)":
                        name = input("Enter the name to search for: ")
                        record = book.find(name)
                        if record:
                            for phone in record.phones:
                                print(phone)
                        else:
                            print("Contact not found.")
                    elif command == "all (9)":
                        book.show_all()
                    elif command == "exit (28)":
                        print("Good bye!")
                        book.save()
                        return False
                    else:
                        print("Command execution pending.")
                else:
                    print("Invalid command number. Please try again.")
            else:
                if user_input in commands:
                    print(f"Executing command: {user_input}")
                    command = user_input
                    if command == "find [name] (1)":
                        name = input("Enter the name to search for: ")
                        record = book.find(name)
                        if record:
                            print(record)
                        else:
                            print("Contact not found.")
                    elif command == "phone [name] (2)":
                        name = input("Enter the name to search for: ")
                        record = book.find(name)
                        if record:
                            for phone in record.phones:
                                print(phone)
                        else:
                            print("Contact not found.")
                    elif command == "all (9)":
                        book.show_all()
                    elif command == "exit (28)":
                        print("Good bye!")
                        book.save()
                        return False
                    else:
                        print("Command execution pending.")
                else:
                    print("Invalid command. Enter 'help' for help.")

    print("Data loaded from file.")
    print("Welcome to the assistant bot!")
    process_input(commands)


if __name__ == "__main__":
    main()


@input_error
def delete(args, book):
    if len(args) == 1:  # if in args 1 arg
        arg = args[0]  # get arg from []
        res = book.delete(arg)
        return res
    elif len(args) == 2:
        name, field = args
        record = book.find(name)
        if field == "phones":
            res = record.remove_phones()
            return res
        elif field == "birthday":
            res = record.remove_birthday()
            return res
        elif field == "email":
            res = record.remove_email()
            return res
        elif field == "address":
            res = record.remove_address()
            return res
        elif field == "notes":
            res = record.remove_notes()
            return res



## --------- Не стирать, колись продовжу --------------------------------
# @input_error
# def find(args, book):
#     print(f"шукати {args}")
#     arg = args[0]
#     if is_looks_date(arg):    # якщо arg схожий на дату
#         print(f"Функція буде шукати date {arg}")
#         for record in book.values():
#             print("record", record)
#     #   record виводить
#             if record.birthday:
#                 print(record.birthday, record.birthday.value, arg, Birthday(arg))
#                 print(type(record.birthday), type(record.birthday.value), type(arg), type(Birthday(arg)))
#                 if Birthday(arg) == record.birthday:
#                     print(True)
# # Треба порівняти birthday з arg і вивести records де це співпада
#     elif is_looks_phone(arg):
#         print(f"Функція буде шукати phone {arg}")
#         #book.find_in_field("phone", arg)
#     elif is_looks_email(arg):
#         print(f"Функція буде шукати email {arg}")
#         #book.find_in_field("email", arg)
#     # Address not aveilable to check:
#     # name
#     else:
#         return "Contact does not exist."

###----------------------------------------------------------------------------

