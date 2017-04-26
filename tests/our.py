import unittest

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name)

class Basket:
    def __init__(self):
        self.books = list()
    def addBook(self, book):
        self.books.append(book)
    def isEmpty(self):
        if self.itemsCount() == 0:
            return True
        else:
            return False
    def itemsCount(self):
        return len(self.books)
    def uniqueBooksCount(self):
        uni = set()
        for x in self.books:
           uni.add(x)
        return len(uni)
    def isBookUnique(self, name):
        return Book(name, 1) in self.books

    def totalPrice(self):
        total =0
        for x in self.books:
            total+=x.price
        return total
    def discountPercent(self):
        count = self.uniqueBooksCount()
        if count <= 1:
            return 0
        elif count == 2:
            return 10
        elif count == 3:
            return 15
        else:
            return 20
    def totalDiscountedPrice(self):
        factor = 1.0 - self.discountPercent() / 100.0
        price = 0.0
        included = list()
        for book in self.books:
            if self.isBookUnique(book) and book not in included:
                price += book.price * factor
                included.append(book)
            else:
                price += book.price
        return price

class BookTest(unittest.TestCase):
    def test_bookCreate(self):
        Book("test", 87)
    def test_hasName(self):
        book = Book("test", 00)
        self.assertIsNotNone(book.name)
    def test_hasPrice(self):
        book = Book("name",23)
        self.assertGreater(book.price, 0.0)
    def test_twoBooksWithSameNameAreEqual(self):
        b1 = Book("Test", 1)
        b2 = Book("Test", 1)
        self.assertEqual(b1, b2)


class BasketTest(unittest.TestCase):
    def test_basketCreatable(self):
        Basket()
    def test_bookIsAddableToBasket(self):
        basket = Basket()
        basket.addBook(Book("Test1", 87))
    def test_newlyCreatedBasketIsEmpty(self):
        basket = Basket()
        self.assertTrue(basket.isEmpty())
    def test_afterBookAddedBasketIsNotEmpty(self):
        basket = Basket()
        basket.addBook(Book("Test1", 87))
        self.assertFalse(basket.isEmpty())

    def test_howManyBooks(self):
        basket = Basket()
        basket.addBook(Book("Test1", 87))
        basket.addBook(Book("Test2", 92))
        self.assertEqual(basket.itemsCount(), 2)
        basket.addBook(Book("Test3", 92))
        self.assertEqual(basket.itemsCount(), 3)
    def test_uniqueBooksCount(self):
        basket = Basket()
        basket.addBook(Book("Test1", 87))
        basket.addBook(Book("Test1", 87))
        self.assertEqual(basket.uniqueBooksCount(),1)
    def test_totalPrice(self):
        basket = Basket()
        basket.addBook(Book("Test1", 88))
        basket.addBook(Book("TestR", 12))
        self.assertEqual(basket.totalPrice(), 100)
    def test_discountPercent(self):
        basket = Basket()
        basket.addBook(Book("tt", 23))
        self.assertEqual(basket.discountPercent(), 0)
        basket.addBook(Book("t2", 35))
        self.assertEqual(basket.discountPercent(), 10)
    def test_totalDiscountedPrice(self):
        basket = Basket()
        basket.addBook(Book("tt", 23))
        self.assertEqual(basket.totalDiscountedPrice(), 23)
        basket.addBook(Book("t2", 35))
        self.assertEqual(basket.totalDiscountedPrice(), (23+35)*0.9)
        basket.addBook(Book("t2", 35))
        self.assertEqual(basket.totalDiscountedPrice(), (23+35)*0.9 + 35)
    def test_isUniqueBook(self):
        basket = Basket()
        basket.addBook(Book("tt", 23))
        self.assertTrue(basket.isBookUnique("tt"), True)

if __name__ == '__main__':
    unittest.main()
