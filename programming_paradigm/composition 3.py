class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def get_info(self):
        return f"Title: {self.title}, Author:{self.author}"
class Library:
    def __init__(self):
        
        self.library=[]
    def add_book(self,book):
        self.library.append(book)
    def list_books(self):
        for book in self.library:
            print(f"Book availabe is {book.get_info()}")
    
book1=Book("greed","philip")
book2=Book("voul","hf")
book3=Book('anase','kofi')

fill=Library()


fill.add_book(book1)
fill.add_book(book2)
fill.add_book(book3)
fill.list_books()