import json
from datetime import datetime

class Book: # Book კლასის შექმნა
    #კლასის სტრუქტურის გაწერა
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
    

    def to_dict(self):
        return {"title": self._title, "author": self._author, "year": self._year}


    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])


    def get_title(self):
        return self._title


    def get_author(self):
        return self._author


    def get_year(self):
        return self._year


class BookManager: # BookManager კლასის შექმნა
    def __init__(self):
        self._books = []

    # წიგნის სახელის შეყვანა-შემოწმება
    def _input_title(self):
        while True: #ციკლი ამოწმებს რომ დასახელება არ იყოს ცარიელი
            title = input("Enter book title: ")
            if title.strip():  # დასახელების შემოწმება რომ ცარიელი არ იყოს
                return title
            else:
                print("Title cannot be empty. Please enter a non-empty title.")
    
    # წიგნის ავტორის შეყვანის შემოწმება
    def _input_author(self):
        while True: #ციკლი ამოწმებს რომ მნიშვნელობა არ იყოს ცარიელი, ასევე მიიღოს მხოლოდ წერტილი, გამოტოვება და ასოები
            author = input("Enter book author: ")
            if not author.strip():
                print("Author cannot be empty. Please enter a non-empty author.")
            elif not all(char.isalpha() or char.isspace() or char == '.' for char in author):
                print("Invalid author name. Please enter a name with only alphabetic characters.")
            else:
                return author

    # ამოწმებს წიგნის გამოცემის წლის მნიშვნელობას, იღებს მხოლოდ რიცხვს
    def _input_year(self):
        while True:
            year = input("Enter the year of publication of the book (1900 to current year): ")
            try:
                year = int(year)

                if not 1900 <= year <= datetime.now().year:
                    print("Invalid year. Please enter a year between 1900 and the current year.")
                else:
                    return year
            except ValueError:
                print("Invalid year format. Please enter a valid number.")

    # ახალი წიგნის დამატება
    def append_book(self):
        title = self._input_title()
        author = self._input_author()
        year = self._input_year()

        # while year > datetime.now().year: #ამოწმებს რომ წელი არ იყოს მიმდინარეზე მეტი
        #     print("Invalid year. Publication year cannot be in the future.")
        #     year = self._input_year()

        new_book = Book(title, author, year)
        self._books.append(new_book)
        print(f'Book "{title}" added successfully')
        self.save_books_to_file() #ინახავს წიგნს ფაილში

    # წიგნის სათაურით ძებნა 
    def search_book_by_title(self, title):
        searched_books = [book for book in self._books if book.get_title().lower() == title.lower()]
        #თუ სათაური ვერ მოიძებნა
        if not searched_books:
            print(f'Book title "{title}" not found')
        else:
            # წარმატებული პოვნის შემთხვევაში გამოიტანს შესაბამის შეტყობინებას
            print(f'Books found with title "{title}": ')
            for book in searched_books:
                print(f"Author: {book.get_author()}, Year of Publishing: {book.get_year()}")

    #სრული სიის ბეჭვდა
    def book_full_list(self):
        if not self._books:
            print("Books list is empty") # თუ სია ცარიელია
        else:
            # სრული სიის დაბეჭვდა ცხრილის სახით
            #ბეჭდავს სათაურს
            print("Books list:")
            print("{:<10} {:<30} {:<25} {:<10}".format("No.", "Title", "Author", "Year"))
            print("-" * 75)
            # ციკლით გადაივლის ყველა წიგნის დასაბეჭდად ცხრილში
            for index, book in enumerate(self._books, start=1):
                print("{:<5} {:<30} {:<30} {:<10}".format(index, book.get_title(), book.get_author(), book.get_year()))


    #მონაცემების ჩაწერა ფაილში და შენახვა
    def save_books_to_file(self):
        ''' for save books in json type file'''
        try:
            with open("books.json", mode="w", encoding="utf-8") as file:
                book_data = [book.to_dict() for book in self._books]
                json.dump(book_data, file, indent=2)
            
        except IOError as ex:
            #თუ მონაცემების შენახვისას წარმოიშვა შეცდომა
            print(f"An error occurred while saving the books to file: {ex}")

    # ჩატვირთვა შენახული ფაილიდან
    def load_books_from_file(self):
        '''load saved book list file'''
        try:
            with open("books.json", mode="r", encoding="utf-8") as file:
                book_data = json.load(file)
                self._books = [Book.from_dict(data) for data in book_data]

        except FileNotFoundError as ex:
            #თუ ვერ ნახავს შენახულ ფაილს გააგრძელებს მუშაობას
            print(f"An error occurred while loading the books from file: {ex}")


def main():
    book_manager = BookManager()
    book_manager.load_books_from_file() # ფაილის არსებობის შემთხვევაში ჩაიტვირთება პროგრამაში

    while True: #ენიუს გამოტანა კონსოლში
        print("\nMenu:")
        print("1. Add new book")
        print("2. View list of all books")
        print("3. Find a book by title")
        print("4. Exit")

        choice = input("Select action (1-4):")

        if choice == '1': # ახალი წიგნის დამატება
            book_manager.append_book()

        elif choice == '2':  # სრული სიის გამოტანა
            book_manager.book_full_list()
        
        elif choice == '3': #ძებნის შედეგის გამოტანა
            title = input("Enter the title of the book to search: ")
            book_manager.search_book_by_title(title)
        
        elif choice == '4':
            book_manager.save_books_to_file() #ფაილში შენახვა პროგრამის გათიშვამდე
            print("Exit the program. Goodbye!")
            break

        else:
            # არასწორი არჩევანის შემთხვევაში გამოიტანოს შეტყობინება
            print("Incorrect choice. Please select from 1 to 4.")


if __name__ == "__main__":
    main()
