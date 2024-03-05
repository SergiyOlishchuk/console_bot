
PHONE_BOOK = {}

def parse_command(command: str, command_list: list) -> tuple:
    command = command.strip()
    if command.lower() in command_list:
        return (command.lower(), )
    
    command = command.split(' ')
    command[0] = command[0].lower()
    if command[0] in command_list:
        return tuple(command)
    else:
        return tuple()

def input_error(handler):
    def wrapper(*args):
        try:
            res = handler(*args)
        except KeyError:
            res = 'Unknown user name'
        except ValueError:
            res = 'Invalid data'
        except IndexError:
            res = 'Invalid count of parameters'

        return res
    return wrapper


def greeting_command(*args) -> str:
    return 'How can I help you?'

@input_error
def add_command(*args) -> str:
    if len(args) != 2:
        raise IndexError
    PHONE_BOOK.update({args[0] : args[1]})
    return 'Add to phone book'

@input_error
def change_command(*args) -> str:
    if len(args) != 2:
        raise IndexError
    PHONE_BOOK[args[0]] = args[1]
    return 'Record changed'

@input_error
def phone_command(*args) -> str:
    if len(args) != 1:
        raise IndexError
    return PHONE_BOOK[args[0]]

def show_all_command(*args) -> str:
    if len(PHONE_BOOK) > 0:
        res = 'Name\tPhone number\n'
        for key, item in PHONE_BOOK.items():
            res += key + '\t' + item + '\n'
        return res.strip()
    else:
        return 'Phone book is empty'
    
def quit_command(*args) -> None:
    print('Good bye!')
    quit()
    

def main():
    commands = {
        'hello' : greeting_command,
        'add' : add_command,
        'change' : change_command,
        'phone' : phone_command,
        'show all' : show_all_command,
        'close' : quit_command,
        'good bye' : quit_command,
        'exit' : quit_command
    }

    while True:
        command = input('Input command: ')
        parsed_command = parse_command(command, commands.keys())

        if len(parsed_command) > 0:
            print(commands[parsed_command[0]](*parsed_command[1:]))
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()