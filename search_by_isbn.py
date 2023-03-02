import json
# Python's built-in module for opening and reading URLs
from urllib.request import urlopen


def main(url):
    # send a request and get a JSON response
    response = urlopen(url)
    # parse JSON into Python as a dictionary
    book_data = json.load(response)

    volume_info = book_data['items'][0]['volumeInfo']
    search_info = book_data['items'][0]['searchInfo']
    image_link = volume_info['imageLinks']
    author = volume_info['authors']

    prettify_author = author if len(author) > 1 else author[0]

    print(f"\nTitle: {volume_info['title']}")
    print(f"Author: {prettify_author}")
    print(f"Page Count: {volume_info['pageCount']}")
    print(f"Publication Date: {volume_info['publishedDate']}")
    print(f"Description: {search_info['textSnippet']}")
    print(f"Image Link: {image_link['smallThumbnail']}")
    print("\n***\n")


if __name__ == '__main__':
    # sample ISBN for testing: 1593276036
    api = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
    isbn = input('Enter 10 digit ISBN: ').strip()
    main(api+isbn)
