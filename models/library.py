class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + " by " + self.author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def getitem(self, index):
        return self.books[index]

    def by_author(self, author):
        book_list = []
        for book in self.books:
            if book.auhtor == author:
                book_list.append(book)
        if not book_list:
            raise KeyError('Author does not exist')
        return book_list

    def __len__(self):
        return len(self.books)

    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)

        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)

        return authors

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)
