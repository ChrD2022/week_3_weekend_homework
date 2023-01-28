from models.book import Book

book_1 = Book("Dune", "Frank Herbert", "SciFi")
book_2 = Book("American Sniper", "Chris Kyle", "Autobiography")
book_3 = Book("Dracula", "Bram Stoker", "Fantasy")
book_4 = Book("The Twits", "Roald Dahl", "Childrens")
books_checked_in = [book_1, book_2, book_3]
books_checked_out = [book_4]

def add_new_book(the_new_book):
    books_checked_in.append(the_new_book)

def delete_book(selected_book):
    books_checked_in.remove(selected_book)