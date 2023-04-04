# Define a class for Library
class Library:
    # Initialize the library with a list of books
    def __init__(self, books):
        self.books = books
    
    # Define a method to display the available books
    def display_books(self):
        print("The available books are:")
        for book in self.books:
            print(book)
    
    # Define a method to lend a book to a student
    def lend_book(self, book, student):
        # Check if the book is in the library
        if book in self.books:
            # Remove the book from the library
            self.books.remove(book)
            # Add the book and student to a dictionary of borrowed books
            self.borrowed_books[book] = student
            print(f"{book} has been lent to {student}.")
        else:
            # Print a message if the book is not available
            print(f"{book} is not available.")
    
    # Define a method to return a book to the library
    def return_book(self, book):
        # Check if the book is in the borrowed books dictionary
        if book in self.borrowed_books:
            # Remove the book and student from the dictionary
            student = self.borrowed_books.pop(book)
            # Add the book back to the library
            self.books.append(book)
            print(f"{book} has been returned by {student}.")
        else:
            # Print a message if the book is not borrowed
            print(f"{book} is not borrowed.")

# Define a class for Student
class Student:
    # Initialize the student with a name and an empty list of books
    def __init__(self, name):
        self.name = name
        self.books = []
    
    # Define a method to request a book from the library
    def request_book(self):
        # Ask the user for the name of the book
        book = input(f"{self.name}, enter the name of the book you want to borrow: ")
        return book
    
    # Define a method to return a book to the library
    def return_book(self):
        # Ask the user for the name of the book
        book = input(f"{self.name}, enter the name of the book you want to return: ")
        return book
    
    # Define a method to add a book to the student's list of books
    def add_book(self, book):
        self.books.append(book)
    
    # Define a method to remove a book from the student's list of books
    def remove_book(self, book):
        self.books.remove(book)

# Create an instance of Library with some books
library = Library(["Python for Beginners", "Learn Java", "Data Structures and Algorithms", "Web Development with Django"])

# Create an instance of Student with a name
student = Student("Alice")

# Display the menu options
print("Welcome to the Library Management System")
print("1. Display Books")
print("2. Request Book")
print("3. Return Book")
print("4. Exit")

# Loop until the user chooses to exit
while True:
    # Ask the user for their choice
    choice = int(input("Enter your choice: "))
    
    # Perform different actions based on the choice
    if choice == 1:
        # Display the available books
        library.display_books()
    elif choice == 2:
        # Request a book from the library
        requested_book = student.request_book()
        # Lend the book to the student if possible
        library.lend_book(requested_book, student.name)
        # Add the book to the student's list of books if possible
        student.add_book(requested_book)
    elif choice == 3:
        # Return a book to the library
        returned_book = student.return_book()
        # Return the book to the library if possible
        library.return_book(returned_book)
        # Remove the book from the student's list of books if possible
        student.remove_book(returned_book)
    elif choice == 4:
        # Exit the program
        print("Thank you for using the Library Management System.")
        break
    else:
        # Print an invalid choice message
        print("Invalid choice. Please try again.")