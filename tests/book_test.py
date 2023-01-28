import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("Dune", "Frank Herbert", "SciFi")

    def test_book_has_a_name(self):
        self.assertEqual("Dune", self.book.title)
    
    def test_book_has_an_author(self):
        self.assertEqual("Frank Herbert", self.book.author)
    
    def test_book_assigned_a_genre(self):
        self.assertEqual("SciFi", self.book.genre)
