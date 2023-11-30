import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search all books',
    2: 'Search by Title',
    3: 'Search by Publisher',
    4: 'Search by Price Range (min and max)',
    5: 'Search by Title and Publisher',
    6: 'Exit',
}


def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()
    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item['ISBN'], item['title'])
    print("The end of books.")


def search_by_title():
    title = input("What is the exact book title that you are looking for?\n")
    results = list(book_dao.findByTitle(title))
    # Display results
    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("The title you wanted does not exist in our database.")
    print("The end.")


def search_by_publisher():
    publisher = input("Enter the publisher name to search for books:\n")
    results = list(book_dao.findByPublisher(publisher))
    # Display results
    if len(results) > 0:
        print("Books published by", publisher, ":")
        for book in results:
            print(book['ISBN'], book['title'])
    else:
        print("No books found for the publisher:", publisher)
    print("The end.")


def search_by_price_range():
    try:
        min_price = float(input("Enter the minimum price:\n"))
        max_price = float(input("Enter the maximum price:\n"))
    except ValueError:
        print("Please enter valid numbers for price.")
        return
    results = list(book_dao.findByPriceRange(min_price, max_price))
    # Display results
    if len(results) > 0:
        print(f"Books in the price range {min_price} to {max_price}:")
        for book in results:
            print(book['ISBN'], book['title'], "- Price:", book['price'])
    else:
        print(f"No books found in the price range {min_price} to {max_price}.")
    print("The end.")


def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print(str(key) + '.', menu_options[key], end="  ")
    print()
    print("The end of top-level options")
    print()


def print_search_menu():
    print()
    print("Please make a selection")
    for key in search_menu_options.keys():
        print(str(key)+'.', search_menu_options[key], end="  ")
    print()
    print("The end of search menu options")
    print()


def option1():
    print('Handle option \'Option 1\'')


def option2():
    print('Handle option \'Option 2\'')


def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    # print_search_menu
    print_search_menu()

    # user selection of options and actions
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        print('Search Option 1: all books were chosen.')
        search_all_books()
    elif option == 2:
        print('Search Option 2: search books by title.')
        search_by_title()
    elif option == 3:
        print('Search Option 3: search books by publisher.')
        search_by_publisher()
    elif option == 4:
        print('Search Option 3: search books by price range.')
        search_by_price_range()


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        # More options to be added
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
