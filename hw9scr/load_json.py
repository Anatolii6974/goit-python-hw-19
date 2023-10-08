from models import *
import json

# Функція для завантаження даних авторів з JSON-файлу
def load_authors(filename):
    with open(filename, 'r') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author(**author_data)
            author.save()

# Функція для завантаження цитат з JSON-файлу та пов'язання їх з авторами
def load_quotes(filename):
    with open(filename, 'r') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data['author']
            author = Author.objects(fullname=author_name).first()
            if author:
                quote_data['author'] = author
                quote = Quote(**quote_data)
                quote.save()


if __name__ == '__main__':
    # Завантаження даних з файлів
    load_authors('authors.json')
    load_quotes('quotes.json')	    