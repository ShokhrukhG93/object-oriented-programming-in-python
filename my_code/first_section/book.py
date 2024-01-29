class Book:
    def __init__(self, isbn, title, author, publisher,
                 pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher  
        self.pages = pages
        self._price = price
        self.copies = copies

    def display(self):
        print(f"Book's title: {self.title}")
        print(f"Book's isbn: {self.isbn}")
        print(f"Book's price: {self._price}")
        print(f"Number of book's copies: {self.copies}")
        print('_' * 50)

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print(f"The book '{self.title}' is out of stock")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError("Price cannot be less than 50 or more than 1000")


if __name__ == "__main__":
    book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
    book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
    book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
    book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

    book1.display()
    book2.display()
    book3.display()
    book4.display()

    book3.sell()
    book3.sell()
    book3.sell()
    book3.sell()
    book3.sell()
    book3.sell()

    books = [book1, book2, book3, book4]

    for book in books:
        book.display()

    books_title = [book.title for book in books]

    print(books_title)
    book1.price = 100000
