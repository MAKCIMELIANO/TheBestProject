import requests as req
from bs4 import BeautifulSoup as BS, BeautifulSoup

resp = req.get("https://www.work.ua/jobs-kyiv-python/")

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.h2)
print(soup.h2.text)
print(soup.h2.parent)
#url = ("https://www.work.ua/jobs-kyiv-python/")

