import json
# Python's built-in module for opening and reading URLs
from urllib.request import urlopen

import url_generation


if __name__ == '__main__':
    url = url_generation.url_generation()
    response = urlopen(url)
    book_data = json.load(response)

    totalitems = book_data['totalItems']
    items_list = book_data['items']
    print('件数：', totalitems)

    for item in items_list:
        info = item.get('volumeInfo', 'unknown')
        title = info.get('title', 'unknown')
        author = info.get('authors', 'unknown')
        publisher = info.get('publisher', 'unknown')
        publisheddate = info.get('publishedDate', 'unknown')
        pages = info.get('pageCount', 'unknown')
        printtype = info.get('printType', 'unknown')
        description = info.get('description', 'unknown')
        language = info.get('language', 'unknown')

        print('タイトル：', title)
        print('著者：', author)
        print('出版社：', publisher)
        print('出版日：', publisheddate)
        print('ページ数：', pages)
        print('種別：', printtype)
        print('言語：', language)
        print('要約：', description)
        print('\n******************************\n')
