class some_shit(KeyError,ValueError,IndexError):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        print(*args)
        try:
            return func(*args, **kwargs)       
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me name and phone KEY."
        except IndexError:
            return "Give me name and phone INDEX."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):  
    name, phone = args
    contacts[name] = phone
    return "Contact added."
   

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact wasn't found. Please try it again."

@input_error
def show_phone(args, contacts):
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact wasn't found. Please try it again."

@input_error
def show_all(contacts):
    i = 1
    result = ""
    for key, value in contacts.items():
        result += (
            f"{key:^20}: {value:^15}\n"
            if i != len(contacts)
            else f"{key:^20}: {value:^15}"
        )
        i += 1
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
