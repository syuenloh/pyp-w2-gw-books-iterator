from decimal import Decimal


class Book(object):
    def __init__(self, title, authors, prince_amount, price_currency):
        # initialize attributes
        pass

    @property
    def price(self):
        # create an instance of `Price`, using the book's attributes
        pass

    def __str__(self):
        # check the string format in the unit tests
        pass


class Price(object):
    EXCHANGE_RATES = {
        'USD': {
            'EUR': Decimal('0.89'),
            'YEN': Decimal('109.8')
        },
        'EUR': {
            'USD': Decimal('1.13'),
            'YEN': Decimal('123.6')
        },
        'YEN': {
            'USD': Decimal('0.0091'),
            'EUR': Decimal('0.0081')
        },
    }

    def __init__(self, amount, currency='USD'):
        pass

    def __str__(self):
        pass

    def get_currency(self):
        pass

    def __add__(self, other):
        # return a new `Price` instance, representing the sum of
        # both given ones
        pass

    def __eq__(self, other):
        # compare if two prices are equal. Keep in mind that both prices
        # might have different currencies. Use the `.get_value()` function
        # to transform prices to a comparable currency.
        pass

    def __ne__(self, other):
        # opposite to __eq__
        pass

    def get_value(self, currency=None):
        # if no currency is given, returns the current price amount. If a
        # different currency is given, handles the price convertion to the
        # given currency. Use the `EXCHANGE_RATES` dict for that.
        pass


class BookIterator(object):
    def __init__(self, file_path):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        # make sure each execution of __next__ returns an instance
        # of the `Book` class.
        pass

    next = __next__


def read_file_line_by_line(file_path):
    file_lines = []
    file_obj = open(file_path, 'r')
    try:
        line = file_obj.readline()
        while line:
            book_data = [l.strip() for l in line.split(',')]
            file_lines.append(book_data)
            line = file_obj.readline()
    finally:
        file_obj.close()
    return file_lines
