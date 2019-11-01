import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import csv

def pagecount():
    url = "http://quotes.toscrape.com"
    page = "/page/1"
    # allquotes = []
    with open("quotes.csv", "w+", encoding="utf-8") as file:
        # data = writer(file)
        fieldnames = ["quote", "author", "author bio link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        # writer.writerow(fieldnames)
        while page:

            response = requests.get(f"{url}{page}")
            print(f"scraping pages {url}{page}")
            soup = BeautifulSoup(response.text, "html.parser")

            quotes = soup.find_all(class_="quote")

            for quote in quotes:
                squote = quote.find(class_="text").get_text()
                author = quote.find(class_="author").get_text()
                authorlink = quote.find("a")["href"]
                writer.writerow({"quote": squote,
                                 "author": author,
                                 "author bio link": authorlink})
            next_page = soup.find(class_="next")
            page = next_page.find("a")["href"] if next_page else None
            sleep(1)

pagecount()