class Book:
    total_books = 0  # Class variable shared across all instances

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print(f"📚 Total Books: {cls.total_books}")

# Creating Book objects
book1 = Book("The Alchemist")
book2 = Book("1984")
book3 = Book("Atomic Habits")

# Display total number of books
Book.show_total_books()
