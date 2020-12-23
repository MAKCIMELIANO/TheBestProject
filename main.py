import requests as req
from bs4 import BeautifulSoup

resp = req.get("https://www.work.ua/jobs-kyiv-python/")

soup = BeautifulSoup(resp.text, 'lxml')

# print(soup.h2)
# print(soup.h2.text)
# print(soup.h2.parent)
#url = ("https://www.work.ua/jobs-kyiv-python/")

results = soup.find_all('h2')
# # print(results)
for h2 in results:
    print(h2.text.strip())
jobs = []

for link in soup.find_all('h2'):
    # print(link)
    jobs.append({"title": link.text.})

print(jobs)