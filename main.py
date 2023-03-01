import requests

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:9784798161914' #GooglBooksAPI
response = requests.get(url) #情報の取得
print(response)