from datetime import datetime


class Book:
    all = []  # Class attribute to store all book instances
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        """Return a list of related contracts"""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return a list of related authors using the Contract class as an intermediary"""
        return [contract.author for contract in self.contracts()]


class Author:
    all = []  # Class attribute to store all author instances
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        """Return a list of related contracts"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Return a list of related books using the Contract class as an intermediary"""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object between the author and the specified book"""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Return the total amount of royalties the author has earned from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []  # Class attribute to store all contract instances
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author class")
        self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book class")
        self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be an instance of str")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an instance of int")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date as the date passed into the method"""
        if not isinstance(date, str):
            raise Exception("date must be an instance of str")
        return [contract for contract in cls.all if contract.date == date]