import unittest
from decimal import Decimal

from books_iterator.main import Price


class PriceTestCase(unittest.TestCase):
    def test_price_basic_api(self):
        p1 = Price(Decimal('10'), 'USD')
        p2 = Price(Decimal('5.50'), 'EUR')
        p3 = Price(Decimal('2894.2'), 'YEN')

        self.assertEqual(p1.get_currency(), 'USD')
        self.assertEqual(p2.get_currency(), 'EUR')
        self.assertEqual(p3.get_currency(), 'YEN')
        self.assertEqual(p1.get_value(), 10)
        self.assertEqual(p2.get_value(), Decimal('5.5'))
        self.assertEqual(p3.get_value(), Decimal('2894.2'))

    def test_price_conversion(self):
        p1 = Price(Decimal('10'), 'USD')
        p2 = Price(Decimal('5.50'), 'EUR')
        p3 = Price(Decimal('2894.2'), 'YEN')

        self.assertAlmostEqual(p1.get_value('EUR'), Decimal('8.9'), places=2)
        self.assertAlmostEqual(p1.get_value('YEN'), Decimal('1098'), places=2)
        self.assertAlmostEqual(p2.get_value('USD'), Decimal('6.215'), places=2)
        self.assertAlmostEqual(p2.get_value('YEN'), Decimal('679.8'), places=2)
        self.assertAlmostEqual(p3.get_value('USD'), Decimal('26.34'), places=2)
        self.assertAlmostEqual(p3.get_value('EUR'), Decimal('23.44'), places=2)

    def test_price_addition(self):
        p1 = Price(Decimal('10'), 'USD')
        p2 = Price(Decimal('5.50'), 'EUR')
        p3 = Price(Decimal('2894.2'), 'YEN')

        # USD + EUR
        usd_eur = p1 + p2
        self.assertAlmostEqual(
            usd_eur.get_value(), Decimal('16.215'), places=2)

        # USD + YEN
        usd_yen = p1 + p3
        self.assertAlmostEqual(
            usd_yen.get_value(), Decimal('36.34'), places=2)

        # EUR + YEN
        eur_yen = p2 + p3
        self.assertAlmostEqual(
            eur_yen.get_value(), Decimal('28.94'), places=2)

    def test_price_equality(self):
        self.assertEqual(
            Price(Decimal('10'), 'USD'), Price(Decimal('10'), 'USD'))

    def test_price_equality_currencies(self):
        self.assertEqual(
            Price(Decimal('11.3'), 'USD'), Price(Decimal('10'), 'EUR'))
