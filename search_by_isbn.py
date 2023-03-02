import json
# Python's built-in module for opening and reading URLs
from PIL import Image
from urllib.request import urlopen


api = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
isbn = input('Enter 10 digit ISBN: ').strip()

# send a request and get a JSON response
response = urlopen(api + isbn)
# parse JSON into Python as a dictionary
book_data = json.load(response)


total_items = book_data['totalItems']
for i in range(total_items):
    volume_info = book_data['items'][i]['volumeInfo']
    search_info = book_data['items'][i]['searchInfo']
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


