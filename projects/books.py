# libary.py 

# This will hold all our books 
libary =[]

# Function to add a book 
def add_boo(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "read": False,
    }
    libary.append(book)
    print(f'Book "{title}" added!')

# Function to list all the books 
def list_books():
    if not libary:
        print("No books in your libary yet")
    for idxm, book in enumerate(libary, 1):
        status = "Read" if book ["read"] else "NOt read"
        print(f'{idx}. "{book["title"]} by {book["author"]} ({book["year"]}) - {status}"')
