import requests


from lxml import html
from bs4 import BeautifulSoup


url = "https://sg.finance.yahoo.com/quote/ES3.SI/"

with requests.Session() as s:
    result = s.get(url)
    soup = BeautifulSoup(result.content,'lxml')
    paragraph = soup.findAll('tr')
    print(type(paragraph))
    for p in paragraph:
        print(p.text.strip())
        print("\n")


