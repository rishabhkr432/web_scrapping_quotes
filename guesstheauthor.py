import requests
from bs4 import BeautifulSoup
from time import sleep

def pagecount():
    url = []
    for page in range(10):
        if (url == 0):
            url = "http://quotes.toscrape.com"

        else:
            url = ("http://quotes.toscrape.com" + "/page/" + str(page + 1))

        readtext(url, page)


def readtext(url, page):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    pager = soup.find(class_="pager")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        authorlink = quote.find("a")["href"]
        descriptionget = requests.get(("http://quotes.toscrape.com" + authorlink))
        descriptionpage = BeautifulSoup(descriptionget.text, "html.parser")
        authordescription = descriptionpage.find(class_="author-description").contents[0]
        # print(authordescription)

        # description = link.find(class_="author-description")
        # print("Guess the author?")
        print(text)

        while True:
            checkauthor = input("Guess the author?\n")
            first_guess = authordescription.strip()
            if (author in first_guess):
                if (checkauthor == author):
                    print("You won")
                    break
                else:
                    first_guess = first_guess.replace(author, "The author")
                    lines = first_guess.split('.')
                    print("Here is the first hint")
                    print(lines[0] + '.')
                    first_hint = input("Try guessing now\n")
                    if first_hint == author:
                        print("you_won")
                        break
                    print("Here is second hint")
                    print(lines[1] + '.')
                    second_hint = input("Try guessing now\n")
                    if second_hint == author:
                        print("you_won")
                        break
                    else:
                        pass
       # second_guess = first_guess


# if (checkauthor == author):
#     print("You won")
# else:
#     print("This is first hint")

    print(author)
    # print(authorlink)


    print(f"NEXTPAGE{page}")

# print(pager)
pagecount()

# print(type(quotes))
# print(quotes)
