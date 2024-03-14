from src.classes import AddressBook
from src.services import parse_input, add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays, show_commands, add_address, edit_address, show_address,remove_address
from src.disk import save_to_json, load_from_json

def main():
    # book = AddressBook()
    # print(book)
    try:
        book = load_from_json()
        print("main load", book)
    except:
        book = AddressBook()
        print("main new", book)

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            save_to_json(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(show_commands())
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            birthdays(book)
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "edit-address":
            print(edit_address(args, book))
        elif command == "show-address":
            print(show_address(args,book))
        elif command == "remove-address":
            print(remove_address(args, book))
        else:
            print("Invalid command. Enter \"help\" for help")

if __name__ == "__main__":
    main()

# Comment
    