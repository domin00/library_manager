import datetime
import sqlite3
import csv


class LibraryManager:
    """A class that manages a library using SQL."""

    def __init__(self):
        """Initializes the library manager."""
        self.books = []
        self.borrowers = []
        self.checkouts = []

            # Connect to the database.
        self.db_path = 'books.db'
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Check if the tables exist.
        tables = ["books", "users", "checkouts"]
        for table in tables:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
            if not cursor.fetchone():
                if table == 'books':
                    # Create the tables.
                    cursor.execute("""CREATE TABLE books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR(255) NOT NULL,
                        author VARCHAR(255) NOT NULL,
                        genre VARCHAR(255) NOT NULL
                    )""")
                elif table == 'users':
                    cursor.execute("""CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone_number VARCHAR(255) NOT NULL
        )""")
                elif table == 'checkouts':
                    cursor.execute("""CREATE TABLE checkouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            checked_out_on DATETIME NOT NULL,
            due_back_on DATETIME NOT NULL,
            returned_on DATETIME
        )""")
                    
        # Save the changes to the database.
        conn.commit()

        # Close the connection to the database.
        conn.close()

        


    def import_batch_of_books(self, path_in):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        with open(path_in, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")

            for row in reader:
                string = f"INSERT INTO books (title, author, genre) VALUES ('{row[0]}', '{row[1]}', '{row[2]}')"
                cursor.execute(string)

        # Save the changes to the database.
        conn.commit()

        # Close the connection to the database.
        conn.close()



    def add_book(self, title, author, genre):
        """Adds a new book to the library."""
        new_book = {
            "title": title,
            "author": author,
            "genre": genre,
        }
        self.books.append(new_book)

    def add_user(self, title, author, genre):
        """Adds a new book to the library."""
        new_book = {
            "title": title,
            "author": author,
            "genre": genre,
        }
        self.books.append(new_book)

    def check_out_book(self, book_id, borrower_id):
        """Checks out a book to a borrower."""
        book = self.get_book_by_id(book_id)
        borrower = self.get_borrower_by_id(borrower_id)

        if book is None:
            print("Book with ID {} does not exist.".format(book_id))
            return

        if borrower is None:
            print("Borrower with ID {} does not exist.".format(borrower_id))
            return

        if book in self.checkouts:
            print("Book {} is already checked out.".format(book["title"]))
            return

        checkout = {
            "book_id": book_id,
            "borrower_id": borrower_id,
            "checked_out_on": datetime.now(),
        }
        self.checkouts.append(checkout)

    def return_book(self, checkout_id):
        """Returns a book to the library."""
        checkout = self.get_checkout_by_id(checkout_id)

        if checkout is None:
            print("Checkout with ID {} does not exist.".format(checkout_id))
            return

        book = self.get_book_by_id(checkout["book_id"])
        borrower = self.get_borrower_by_id(checkout["borrower_id"])

        book["checked_out_on"] = None
        borrower["checked_out_books"].remove(checkout["book_id"])

        self.checkouts.remove(checkout)

    def list_all_books(self):
        """Lists all books in the library."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get all the books from the books table.
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        # Print all the books.
        for book in books:
            print(book)

        # Close the connection to the database.
        conn.close()

    def get_book_by_id(self, book_id):
        """Gets a book by ID."""
        for book in self.books:
            if book["id"] == book_id:
                return book

        return None

    def get_borrower_by_id(self, borrower_id):
        """Gets a borrower by ID."""
        for borrower in self.borrowers:
            if borrower["id"] == borrower_id:
                return borrower

        return None

    def get_checkout_by_id(self, checkout_id):
        """Gets a checkout by ID."""
        for checkout in self.checkouts:
            if checkout["id"] == checkout_id:
                return checkout

        return None
