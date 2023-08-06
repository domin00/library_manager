import sys

from library_management import LibraryManager

def main():
    """Starts the library management system."""

    library_manager = LibraryManager()

    while True:
        print("What would you like to do?")
        print("1. Add a book")
        print("2. Check out a book")
        print("3. Return a book")
        print("4. List all books")
        print("5. Import new books")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library_manager.add_book()
        elif choice == "2":
            library_manager.check_out_book()
        elif choice == "3":
            library_manager.return_book()
        elif choice == "4":
            library_manager.list_all_books()
        elif choice == "5":
            csv_path = input("CSV Path to Books: ")
            library_manager.import_batch_of_books(csv_path)
        elif choice == "q":
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
