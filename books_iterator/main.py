from decimal import Decimal


class Book(object):
    def __init__(self, title, authors, prince_amount, price_currency):
        # initialize attributes
        self.title = title
        self.authors = authors
        self.prince_amount = prince_amount
        self.price_currency = price_currency

    @property
    def price(self):
        # create an instance of `Price`, using the book's attributes
        return Price(self.prince_amount, self.price_currency)

    def __str__(self):
        # check the string format in the unit tests
        return "{title} (by {authors}) - {currency}${price}".format(
            title=self.title, authors=self.authors,
            currency=self.price_currency, price=self.prince_amount)


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
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return '{} {}'.format(self.currency, self.amount)

    def get_currency(self):
        return self.currency

    def __add__(self, other):
        # return a new `Price` instance, representing the sum of
        # both given ones
        other_amount = other.get_value(self.currency)
        return Price(self.amount + other_amount, self.currency)

    def __eq__(self, other):
        # compare if two prices are equal. Keep in mind that both prices
        # might have different currencies. Use the `.get_value()` function
        # to transform prices to a comparable currency.
        other_amount = other.get_value(self.currency)
        return self.amount == other_amount

    def __ne__(self, other):
        # opposite to __eq__
        return not (self == other)

    def get_value(self, currency=None):
        # if no currency is given, returns the current price amount. If a
        # different currency is given, handles the price convertion to the
        # given currency. Use the `EXCHANGE_RATES` dict for that.
        if not currency or currency == self.currency:
            return self.amount

        exchange_rate = self.EXCHANGE_RATES[self.currency][currency]
        return self.amount * exchange_rate


class BookIterator(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_obj = None

    def __iter__(self):
        if not self.file_obj or self.file_obj.closed:
            self.file_obj = open(self.file_path, 'r')
        self.file_obj.seek(0)
        return self

    def __next__(self):
        # make sure each execution of __next__ returns an instance
        # of the `Book` class.
        line = self.file_obj.readline()
        if not line:
            raise StopIteration()
        book_data = [l.strip() for l in line.split(',')]
        book = Book(*book_data)
        return book

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
