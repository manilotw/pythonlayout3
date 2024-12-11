import requests
import os

for id in range(1, 11):
    url = f'https://tululu.org/txt.php?id={id}'

    response = requests.get(url)
    response.raise_for_status()

    os.makedirs('books', exist_ok=True)
    filename = f'books/book{id}.txt'

    with open(filename, 'wb') as file:
        file.write(response.content)