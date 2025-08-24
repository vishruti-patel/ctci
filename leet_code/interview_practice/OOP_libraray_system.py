"""
Practice Inheritance, polymorphism, super(). Create 2 class- Member and Librarian with dedicateds roles and access.
"""


class Member:
    def __init__(self, name):
        self.name = name

    def view_books(self, all_books):
        print(f'\nWelcome {self.name}. Here are the list of books:')
        
        for book in all_books:
            print(book)

all_books = ['5 am Club', 'Atomic Habits', 'Rich Dad Poor Dad']

class Librarian(Member):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.id = employee_id

    def add_books(self, book, all_books):
        all_books.append(book)
        print(f'{book} is added to the list')

    def remove_book(self, book, all_books):
        if book in all_books:
            all_books.remove(book)
            print(f'{book} removed from the list')
        else:
            print(f'Book not found')

    def show_employee_info(self):
        print(f'Name of the employee: {self.name}.\nYour employee id : {self.id}')



def main():
    name = input('Enter your name: ')
    role = input('Enter your role: ').strip().lower()

    if role == 'member':
        user = Member(name)
    elif role == 'librarian':
        id = input('Enter your employee id: ')
        user = Librarian(name, id)
        user.show_employee_info()
    else:
        print('Invalid role')
        return
    
    while True:
        print("\nMenu:")
        print('1. View Books')
        if isinstance(user, Librarian):
            print('2. Add Books')
            print('3. Remove Books')
        print('0. Exit')


        choice = input('Enter your option:')

        if choice == '1':
            user.view_books(all_books)

        elif choice == '2' and isinstance(user, Librarian):
            book = input('Enter book to add: ')
            user.add_books(book, all_books)

        elif choice == '3' and isinstance(user, Librarian):
            remove_book = input('Enter book to delete: ')
            user.remove_book(remove_book, all_books)

        elif choice == '0':
            print('Goodbye!')
            break

        else:
            print('Invalid option')

main()




