class Book:

    def __init__(self, title,author, text):
        self.title = title
        self.author = author
        self.text = text

    def __repr__(self):
        return f"Book: {self.title}, by {self.author}"

    def __add__(self, other):
        return Book(self.title + ' & ' + other.title, self.author + ' & ' + other.author, self.text + ' \n ' + other.text)

    def __len__(self):
        return len(self.text)

    def __mul__(self, other):
        if type(other) == int:
            return [self] *other
        elif isinstance(other, Book):
            return [self]*len(other)
        else:
            raise TypeError ("Unsupported operation")

    def __gt__(self, other):
        if isinstance(other, Book):
            return len(self) > len(other)

    def __iter__(self):
        self.sentences = self.text.split('. ')
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.sentences):
            raise StopIteration
        else:
            out = self.sentences[self.i]
            self.i += 1
            return out


zohar = Book("Zohar", "The Rashbi", "WEHBFUERF. WRGAdfbsd. weverwb" )
LoTR = Book("Lord of the Rings", "J.R.R. Tolkien", ".....")


# print(zohar)
# print(zohar + LoTR)
# print(zohar*3)
# print(zohar*LoTR)
# print(zohar>LoTR)

for something in zohar:
    print(something)