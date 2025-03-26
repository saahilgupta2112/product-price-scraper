import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])

print("Scraped data saved to books.csv")
