import requests
import os
from pathvalidate import sanitize_filename, sanitize_filepath
from bs4 import BeautifulSoup

def check_for_redirect(response):

    if response.history:
        raise requests.exceptions.HTTPError
    
    return response
        
os.makedirs('books', exist_ok=True)

def download_txt(url, filename, folder='books/'):
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(folder, exist_ok=True)

    filename = sanitize_filename(f'{filename}.txt')
    filepath = sanitize_filepath(os.path.join(folder, filename))

    with open(filepath, 'wb') as file:
        file.write(response.content)
 

for id in range(1, 11):

    # url = f'https://tululu.org/txt.php?id={id}'

    url = f'https://tululu.org/b{id}/'

    response = requests.get(url)
    response.raise_for_status()

    try:
        
        check_for_redirect(response)

        soup = BeautifulSoup(response.text, 'lxml')
      
        title = soup.find('h1').text.split('::')[0].strip('\xa0 ')
        filename = f'{id}.{title}'
        
        download_txt(f'https://tululu.org/txt.php?id={id}', filename)

    except:
        pass
  
        