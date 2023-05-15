FILE_NAME = 'guest_book.txt'


def get_guest_name():
    while True:
        your_name = input('Guest name: ')
        return your_name


def collect_guest_names(the_filename):
    while True:
        name = get_guest_name()
        if name == 'q':
            break
        print(f'Welcome, {name.title()}!')
        with open(the_filename, 'a', encoding='utf-8') as the_file_object:
            the_file_object.write(f'{name.title()} visited our event.\n')


if __name__ == '__main__':
    print('Enter guest names.')
    print('Enter "q" to quit.')
    collect_guest_names(FILE_NAME)