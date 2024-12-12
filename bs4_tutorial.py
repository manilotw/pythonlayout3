import requests
from bs4 import BeautifulSoup
import os
from pathvalidate import sanitize_filename, sanitize_filepath


url = 'https://tululu.org/b1/'

responce = requests.get(url)
responce.raise_for_status()

soup = BeautifulSoup(responce.text, 'lxml')
post_title = soup.find('h1').text.split('::')
# photo_url = soup.find('img', class_='attachment-post-image')['src']
# post_text = soup.find('main').find('div', class_='entry-content').text

print('Заголовок книги:', post_title[0].strip('\xa0 '))
print('Автор книги:', post_title[1].strip('\xa0 '))
# print(photo_url)
# print()
# print(post_text)

