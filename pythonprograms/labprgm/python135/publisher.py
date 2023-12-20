class Publisher:
    def __init__(self,name):
        self.n=name

    def show(self):
        pass

class Book(Publisher):
    def __init__(self,title,author,name):
        self.t=title
        self.a=author
        Publisher.__init__(self,name)
    def show(self):
        pass

class Python(Book):
    def __init__(self,price,no_of_pages,title,author,name):
        self.p=price
        self.np=no_of_pages
        Book.__init__(self,title,author,name)
    def show(self):
        print("Book Title:",self.t)
        print("Author:",self.a)
        print("Publisher:",self.n)
        print("Price: Rs.",self.p)
        print("Number of pages: ",self.np)

b1=Python(499,679,"Wolves of Fire","GV Rossum","OXFORD BOOKS")
b1.show()

