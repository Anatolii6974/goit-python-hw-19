import requests
from bs4 import BeautifulSoup
import json


# Function to get information quotes and authors from a page
def scrape_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = []
    authors = []
    
    # Receiving quotes
    quote_divs = soup.find_all(class_='quote')
    for quote_div in quote_divs:
        quote_text = quote_div.find(class_='text').text
        quote_author = quote_div.find(class_='author').text
        quote_tags = [tag.text for tag in quote_div.find_all(class_='tag')]

        quotes.append({
            'tags': quote_tags,
            'author': quote_author,
            'quote': quote_text
        })

        # Information about the authors
        author_link = quote_div.find('a')['href']
        author_url = f'http://quotes.toscrape.com{author_link}'
        author_info = scrape_author(author_url)
        authors.append(author_info)
        
    # print(f'{quotes=}, {authors=}')
    return quotes, authors

def scrape_author(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    author_name = soup.find(class_='author-title').text.strip()
    author_birthdate = soup.find(class_='author-born-date').text.strip()
    author_birthplace = soup.find(class_='author-born-location').text.strip()
    author_description = soup.find(class_='author-description').text.strip()

    return {
        'fullname': author_name,
        'born_date': author_birthdate,
        'born_location': author_birthplace,
        'description': author_description
    }

    

# We receive information from the page and save it in the JSON files
if __name__ == '__main__':
    base_url = "http://quotes.toscrape.com"
    quotes_data, authors_data = [], []
    page_number = 1

    while True:
        url = f"{base_url}/page/{page_number}/"
        
        quotes, authors = scrape_quotes(url)

        if not quotes:
            break

        quotes_data.extend(quotes)
        authors_data.extend(authors)
        page_number += 1

    
    # Load information in JSON files
    with open('quotes.json', 'w') as quotes_file:
        json.dump(quotes_data, quotes_file, indent=2)

    with open('authors.json', 'w') as authors_file:
        json.dump(authors_data, authors_file, indent=2)

    # print(f"{quotes_data=}{authors_data=}")