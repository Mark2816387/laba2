print("пример функции выводящий список книг, выводит их названия: ")
def book_list(books, func):
    for book in books:
        print(func(book))
books = ['System Design','Python и DevOps','Git. Практическое руководство','book of bash']
book_list(books, lambda book: book.upper() + ' - прочитано')
