from decimal import Decimal

class Book(object):
    def __init__(self, title, authors, price_amount, price_currency):
        # initialize attributes
        self.title=title
        self.authors=authors
        self.price_amount=price_amount
        self.price_currency=price_currency
        self._price=None

    @property
    def price(self):
        # create an instance of `Price`, using the book's attributes
        self._price = Price(self.price_amount,self.price_currency)
        return self._price

    def __str__(self):
        # check the string format in the unit tests
        return "{} (by {}) - {}${}".format(self.title,self.authors,self.price_currency,self.price_amount)


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
        self.amount=amount
        self.currency=currency

    def __str__(self):
        return "Price(Decimal('{}'), '{}')".format(self.amount,self.currency)

    def get_currency(self):
        return self.currency

    def __add__(self, other):
        # return a new `Price` instance, representing the sum of
        # both given ones
        if self.currency==other.currency:
            sum_amount=self.amount+other.amount
        else: 
            sum_amount=self.amount+other.get_value(self.currency)
        return Price(sum_amount,self.currency)

    def __eq__(self, other):
        # compare if two prices are equal. Keep in mind that both prices
        # might have different currencies. Use the `.get_value()` function
        # to transform prices to a comparable currency.
        if self.currency==other.currency and self.amount==other.amount:
            return True
        elif self.currency!=other.currency:
            if self.amount==other.get_value(self.currency):
                return True

    def __ne__(self, other):
        # opposite to __eq__
        if self.currency==other.currency and self.amount==other.amount:
            return True
        elif self.currency!=other.currency:
            if self.amount==other.get_value(self.currency):
                return True

    def get_value(self, currency=None):
        # if no currency is given, returns the current price amount. If a
        # different currency is given, handles the price convertion to the
        # given currency. Use the `EXCHANGE_RATES` dict for that.
        if not currency:
            return self.amount
        if currency=='USD':
            return Decimal(self.amount*(self.EXCHANGE_RATES[self.currency]['USD']))
        elif currency=='EUR':
            return Decimal(self.amount*(self.EXCHANGE_RATES[self.currency]['EUR']))
        elif currency=='YEN':
            return Decimal(self.amount*(self.EXCHANGE_RATES[self.currency]['YEN']))


class BookIterator(object):
    def __init__(self, file_path):
        self.file_path=file_path
        self.items=[Book(x[0],x[1],x[2],x[3]) for x in read_file_line_by_line(self.file_path)]
        self.max=len(self.items)

    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        # make sure each execution of __next__ returns an instance
        # of the `Book` class.
        if self.index < self.max:
            book = self.items[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

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
