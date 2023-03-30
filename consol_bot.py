from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
 
 
class Record():
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else []
        
    def add_phone(self, phone):
        self.phones.append(phone)
        
    def edit_phone(self, phone_index, new_phone):
        self.phones[phone_index] = new_phone
        
    def delete_phone(self, phone_index):
        del self.phones[phone_index]


class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        

class Name(Field):
    pass


class Phone(Field):
    pass


# address_book = {}
address_book = AddressBook()


def input_error(func):
     def inner(*args, **kwargs):
         try:
             return func(*args, **kwargs)
         except KeyError:
             return "Contact not found"
         except ValueError:
             return "Please enter name and phone number separated by space"
         except IndexError:
             return "Please enter contact name"
         except:
             return "An error occurred"
     return inner


@input_error
def add_contact(name, phone):
    name = Name(name.lower())
    phone = Phone(phone)
    rec = Record(name, phone)
    address_book.add_record(rec)
    return f"Contact {name} with phone number {phone} has been added"


@input_error
def change_contact(name, phone):
    address_book[name.lower()] = phone
    return f"Phone number for {name} has been changed to {phone}"
@input_error
def get_phone(name):
    return address_book[name.lower()]
def show_all():
    if not address_book:
        return "Phone book is empty"
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in address_book.items())


def handle_command(command):
     command = command.lower()
     if command == "hello":
         return "How can I help you?"
     elif command in ("good bye", "close", "exit"):
         return "Good bye!"
     elif command.startswith("add"):
         parts = command.split()
         if len(parts) < 3:
             return "Please enter contact name and phone number"
         _, name, phone = parts
         return add_contact(name, phone)
     elif command.startswith("change"):
         parts = command.split()
         if len(parts) < 3:
             return "Please enter contact name and phone number"
         _, name, phone = parts
         return change_contact(name, phone)
     elif command.startswith("phone"):
         parts = command.split()
         if len(parts) < 2:
             return "Please enter contact name"
         _, name = parts
         return get_phone(name)
     elif command == "show all":
         return show_all()
     else:
         return "Unknown command"


def main():
     while True:
         command = input("Enter command: ")
         result = handle_command(command)
         print(result)
         if result == "Good bye!":
             break
         
         
if name == '__main__':
     main()