import requests
from bs4 import BeautifulSoup

# using html file:
# with <td> ... </td>
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    print('Data printed with <td> ... </td>')
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            print(td)

# without <td> ... </td>
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    print('\nData printed without <td> ... </td>')
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            print(td.text)

# data printed in a list of 3 elements
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    print('\nData printed in a list of 3 elements:')
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        print(values)

# data stored in a list of list
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    data = []
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    print(data)

# get data only where rows are marked as special
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    data = []
    for tr in soup.find_all('tr', {'class': 'special'}):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    print('\nSpecial data:\n{}'.format(data))

# get data within a specific element
with open('scrape.html') as source:
    soup = BeautifulSoup(source, 'lxml')
    data = []
    div = soup.find('div', {'class': 'special_table'})
    for tr in div.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    print('\nSpecific data:\n{}'.format(data))
