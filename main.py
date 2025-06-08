import requests
from bs4 import BeautifulSoup
import csv

def web_scrap_csv():
    url = input('Enter URL you would like to scrape: ')
    num_pages = int(input('How many pages would you like to scrape?: '))
    file_name = input('Please enter a name for your csv file (no extension): ') + '.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])
        for page in range(1, num_pages + 1):
            page_url = url.rstrip('/') + f'/page/{page}'
            response = requests.get(page_url)
            if response.status_code != 200:
                print(f'Page {page} failed to load.')
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            if not quotes:
                print(f'No quotes found on page {page}.')
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                writer.writerow([text, author])
            print(f'Page {page} successfully scraped.')
        print(f'Data successfully saved to {file_name}.')

def menu():
    while True:
        print('---WELCOME TO WEB SCRAPING CSV---')
        print('What would you like to do?')
        print('1. Scrape a new URL')
        print('2. Exit')
        user_choice = input('Please type "1" or "2": ')
        if user_choice == '1':
            web_scrap_csv()
        elif user_choice == '2':
            print('---Exiting...---')
            print('---Thank you for using WEB SCRAPING CSV---')
            break
        else:
            print('---Invalid response, please type "1" or "2": ---')

if __name__ == '__main__':
    menu()
