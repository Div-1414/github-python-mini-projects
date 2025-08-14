# First function to create book library
def add(n):
    for i in range(n):
        data = input(f"Enter Book Name for book {i+1}: ")
        books.append(data)

# Second function to print book library
def printbook():
    for i in range(len(books)):
        print(f"Book {i+1} = {books[i]}")

# Third function to add a new book to the library
def addbook():
    newbook = input("Enter the book name you want to add: ")
    books.append(newbook)
    print("New Book added 📗")

# Fourth function to remove a book from the library
def removebook():
    r = input("Enter the book name you want to remove: ")
    for book in books:
        if book.lower() == r.lower():
            books.remove(book)
            print("Book Removed 🫡")
            return
    print("No such book in the library ❌❌")

# Fifth function to clear the entire library
def deletelib():
    confirm = input("Are you sure you want to delete the whole library? (yes/no): ").lower()
    if confirm == "yes":
        books.clear()
        print("Library Deleted ☠️☠️")
        return True
    else:
        print("Deletion canceled")
        return False

# Sixth function to save all books to a text file
def savelibrary():
    z = input("Enter the file name you want to create (include .txt): ")
    try:
        with open(z, "w") as file:
            for i in range(len(books)):
                g = f"Book {i+1} = {books[i]}\n"
                file.write(g)
        print("File created successfully 📁📁")
    except Exception as e:
        print("Error creating file:", e)

# Main program
books = []
print("Library System:")
print("****************************************************")

try:
    l = int(input("Enter the number of books you want to enter in Library Memory: "))
    add(l)
except ValueError:
    print("Please enter a valid number.")
    l = 0

while True:
    print('''
************************************************************
➡️ Enter 1 to view books present in the Library.
➡️ Enter 2 to add a new book to the Library.
➡️ Enter 3 to remove a book.
➡️ Enter 4 to delete the Library.
➡️ Enter 5 to save all books to a text file.
➡️ Enter 6 to see the current number of books in the Library.
➡️ Enter 7 to exit.
************************************************************
    ''')
    try:
        c = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number only!")
        continue

    match c:
        case 1:
            printbook()
        case 2:
            addbook()
        case 3:
            removebook()
        case 4:
            if deletelib():
                break
        case 5:
            savelibrary()
        case 6:
            print(f"Current number of books in the Library: {len(books)}")
        case 7:
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm == "yes":
                break
        case _:
            print("Please enter a number from the given choices!")