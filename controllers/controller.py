from flask import render_template, request
from app import app
from models.book import Book
from models.book_list import *

@app.route('/books')
def index():
    return render_template('index.html', title = "CodeCLan Library", books_in = books_checked_in, books_out = books_checked_out)

@app.route('/books', methods=['POST'])
def add_book_to_library():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('index.html', title = "CodeCLan Library", books_in = books_checked_in)

@app.route('/books', methods=[])
def remove_book_from_library():
    
    return render_template('index.html', title = "CodeCLan Library", books_in = books_checked_in)