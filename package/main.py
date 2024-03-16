try:
    from src.classes import AddressBook
    from src.services import *
    from src.disk import save_to_json, load_from_json
except ModuleNotFoundError:
    from .src.classes import AddressBook
    from .src.services import *
    from .src.disk import save_to_json, load_from_json
from termcolor import colored
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

class FirstWordCompleter(Completer):
    def __init__(self, word_list):
        self.word_list = word_list

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        word = text.split(' ')[0]
        
        if ' ' not in text:
            for word in self.word_list:
                if word.startswith(text):
                    yield Completion(word, start_position=-len(text))

commands = [
    'close', 'exit', 'good bye', 'hello', 'help', 'all', 'delete',
    'find-contact', 'add', 'phone', 'change', 'add-birthday', 'show-birthday',
    'change-birthday', 'delete-birthday', 'birthdays', 'add-email', 'email',
    'change-email', 'delete-email', 'add-address', 'change-address',
    'show-address', 'delete-address', 'add-note', 'edit-note', 'delete-note',
    'show-notes'
]





def main():
    try:
        result = load_from_json()  
        if isinstance(result, tuple) and len(result) == 2:
            book, notes = result
        else:
            book = result
            notes = []
    except Exception as e:
        print(f"Failed to load data: {e}")
        book = AddressBook()  
        notes = []


    print("Welcome to the assistant bot!")
    session = PromptSession(completer=FirstWordCompleter(commands))
    # Після визначення функції main() і перед while True:
    while True:
        user_input = session.prompt("Enter a command ===> ").strip()
        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []
        if command in ["close", "exit", "good bye"]:
            save_to_json(book,notes)
            print(colored("Good bye!", 'cyan', attrs=['bold']))
            break
        elif command == "hello":
            print(colored("How can I help you?", 'white', 'on_blue', attrs=['bold']))
        elif command == "help":
            print(show_commands())
# All
        elif command == "all":
            print(show_all(book))#
        elif command == "delete":
            print(delete(args, book))
        # elif command == "find":      # відкладена
        #     print(find(args, book))

# Find  
        elif command == "find-contact":
            print(find(args, book))
        

#Phone
        elif command == "add":
            if len(args) >= 2:
                response = add_contact(args, book) 
                print(colored("✅ " + response, 'green', attrs=['bold']))
            else:
                print(colored("Error: 'add' command requires a name and a phone number.", 'red'))
        elif command == "phone":
            print(show_phone(args, book))#
        elif command == "change":
            print(change_contact(args, book))

#Birthday
        elif command == "add-birthday":
            print(colored(add_birthday(args, book), 'green', attrs=['bold']))
        elif command == "show-birthday":
            print(show_birthday(args, book),'magenta')
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "delete-birthday":
            print(delete_birthday(args, book))       
        elif command == "birthdays":
            birthdays(args, book)
#Email
        elif command == "add-email":
            print(colored(add_email(args, book), 'cyan', attrs=['bold']))
        elif command == "email": 
            print(show_email(args, book))
        elif command == "delete-email":
            print(colored(delete_email(args, book), 'red', attrs=['bold']))

#Address
        elif command == "add-address":
            print(colored(add_address(args, book), 'green', attrs=['bold']))
        elif command == "change-address":
            print(edit_address(args, book))
        elif command == "show-address":
            print(show_address(args,book))
        elif command == "delete-address":
            print(colored(remove_address(args, book), 'red', attrs=['bold']))
# Note
        elif command == "add-note":
            print(colored(show_notes(notes), 'green', attrs=['bold']))
        elif command == "edit-note":
            print(edit_note(notes))
        elif command == "delete-note":
            print(colored(delete_note(notes), 'red'), attrs=['bold'])
        elif command == "show-notes":
            print(show_notes(notes))
            print('=' * 50)

        else:
            print('Invalid command. Enter "help" for help')

if __name__ == "__main__":
    main()