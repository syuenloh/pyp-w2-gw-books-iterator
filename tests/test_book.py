import unittest
from decimal import Decimal

from books_iterator.main import Book, Price


class BookTestCase(unittest.TestCase):

    def test_book_attrs(self):
        b1 = Book('Harry Potter', 'J. K. Rowling', Decimal('20.00'), 'USD')
        self.assertEqual(b1.title, 'Harry Potter')
        self.assertEqual(b1.authors, 'J. K. Rowling')
        self.assertEqual(b1.price_amount, Decimal('20.00'))
        self.assertEqual(b1.price_currency, 'USD')

    def test_book_price(self):
        b1 = Book('Harry Potter', 'J. K. Rowling', Decimal('20.00'), 'USD')
        self.assertEqual(b1.price, Price(Decimal('20.00'), 'USD'))

    def test_book_str_representation(self):
        b1 = Book('Harry Potter', 'J. K. Rowling', Decimal('20.00'), 'USD')
        self.assertEqual(
            str(b1), 'Harry Potter (by J. K. Rowling) - USD$20.00')
