class Publisher:
    publisher = ""
    date = ""
    def __init__(self, publisher, date):
        self.publisher = publisher
        self.date = date

class Book(Publisher):
    title = ""
    author = ""

    def __init__(self, title, author, publisher, date):
        super().__init__(publisher, date)
        self.title = title
        self.author = author

    def set_author(self, author):
        self.author = author


class Python(Book):
    price = 0
    pages = 0

    def __init__(self, title, author, publisher, date, pages, price):
        super().__init__(title, author, publisher, date)
        self.price = price
        self.pages = pages

    def set_author(self, author):
        super().set_author(author)
        print(f"New author set as {self.author}")

    def __str__(self):
        printlines = [f"Book: {self.title}", f"Author: {self.author}", f"Publisher: {self.publisher}"
                      f"Date: {self.date}", f"No. of Pages: {self.pages}", f"Price: {self.price}"]
        return '\n'.join(printlines)

book = Python("Learning Python", "Mark", "Oreally", "03-03-2013", 1783, 850)
book.set_author("Mark Lutz")
print(book)
