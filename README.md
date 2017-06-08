# Books Iterator

Today we will build a simple `Iterator`, to loop through a list of books listed in a CSV file.

Each loop in the iteration, will return an instance of a custom `Book` class that you will also have to implement.

Here's how the `Book` class looks like:

```python
>>> from decimal import Decimal
>>>
>>> book = Book(title='Harry Potter',
                authors='J. K. Rowling',
                price_amount=Decimal('10.00'),
                prince_currency='USD')
>>>
>>> print(book)
'Harry Potter (by J. K. Rowling) - USD$10.00'
```

The interesting part, is that the `Book` price is not a simple float value. It's a dedicated `Price` instance.

```python
>>> print(book.price)
'USD 10.00'
>>>
>>> book.price.get_value()
Decimal('10.0')
>>>
>>> book.price.get_currency()
'USD'
>>>
>>> book.price.get_value('EUR')  # convert to EUR currency
Decimal('8.9')
>>>
```

Once the `Book` and `Price` classes are implemented, you can start working in the books iterator. As mentioned before, the iterator will read content from a CSV file (whaaat!? 😱 How do I read from a file!? Don't worry, we abstracted that part for you, check the `read_file_line_by_line` helper function), convert each line into a `Book` instance, and return it.

This is how it will look like:

```python
>>> books_iterator = BookIterator('books.csv')
>>> it = iter(books_iterator)  # get the actual iterator (calls the __iter__ method)
>>> first_book = next(it)
>>> second_book = next(it)
...
>>> isinstance(first_book, Book)  # True
>>> first_book.title = 'Code Complete'
>>> first_book.price.get_value() = Decimal('27.0')
```
