import unittest
from decimal import Decimal

from books_iterator.main import Book, Price, BookIterator


class BookIteratorTestCase(unittest.TestCase):

    def test_book_iterator_next_method(self):
        books_iterator = BookIterator('books.csv')
        it = iter(books_iterator)
        book = next(it)
        self.assertTrue(isinstance(book, Book))
        self.assertTrue(isinstance(book.price, Price))
        self.assertEqual(book.price.currency, 'USD')

    def test_book_list_comprehension_iteration(self):
        books_iterator = BookIterator('books.csv')
        self.assertEqual(len([b for b in books_iterator]), 7)

    def test_book_for_loop_iteration(self):
        books_iterator = BookIterator('books.csv')
        for book in books_iterator:
            self.assertTrue(isinstance(book, Book))
            self.assertTrue(isinstance(book.price, Price))

    def test_successive_iterations(self):
        books_iterator = BookIterator('books.csv')
        self.assertEqual(len([b for b in books_iterator]), 7)
        self.assertEqual(len([b for b in books_iterator]), 7)
        self.assertEqual(len([b for b in books_iterator]), 7)
