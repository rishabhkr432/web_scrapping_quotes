import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
url = "http://quotes.toscrape.com"
page = "/page/1"
allquotes = []
while page:
    response = requests.get(f"{url}{page}")
    print((f"Scraping pages{url}{page}"))
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        allquotes.append({
            "Quote":quote.find(class_="text").get_text(),
            "Author":quote.find(class_="author").get_text(),
            "authorbiolink":quote.find("a")["href"]
        })
    check_next_page = soup.find(class_="next")
    page = check_next_page.find("a")["href"] if check_next_page else None
    #sleep(2)

quote = choice(allquotes)
print("Here is a Quote:")
print(quote["Quote"])

