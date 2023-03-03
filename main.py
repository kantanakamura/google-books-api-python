import json
# Python's built-in module for opening and reading URLs
from urllib.request import urlopen

import url_generation

def pprint(book_data):
    totalitems = book_data['totalItems']
    items_list = book_data['items']
    print('件数：', totalitems)

    for item in items_list:
        info = item.get('volumeInfo')
        title = info.get('title')
        author = info.get('authors')
        publisher = info.get('publisher')
        publisheddate = info.get('publishedDate')
        pages = info.get('pageCount')
        printtype = info.get('printType')
        description = info.get('description')
        language = info.get('language')
        image = info.get('imageLinks')
        image_link = image.get('thumbnail')

        print('タイトル：', title)
        print('著者：', author)
        print('出版社：', publisher)
        print('出版日：', publisheddate)
        print('ページ数：', pages)
        print('種別：', printtype)
        print('言語：', language)
        print('要約：', description)
        print('画像：', image_link)
        print('\n******************************\n')


if __name__ == '__main__':
    url = url_generation.url_generation()
    response = urlopen(url)
    book_data = json.load(response)
    pprint(book_data)

