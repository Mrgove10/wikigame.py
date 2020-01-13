import ui
from wikipediaPage import wikipediaPage
import requests

# varriable declarations
game = True
roundNumber = 0
randomArticleURl = "https://en.wikipedia.org/wiki/Special:Random"
urlStackTrace = []

#initial pages
startPage = wikipediaPage(randomArticleURl)
goalPage = wikipediaPage(randomArticleURl)

urlStackTrace.append(startPage)
print(urlStackTrace)

ui.startText()
startPage.printLinkOptions()

while game:
    ui.roundText(roundNumber)
    print("Start page :", startPage.title.contents[0])
    print("Goal page :", goalPage.title.contents[0])
    print("Current page :", startPage.title.contents[0])
    # main loop
    choice = input("Your choice : ")

    if choice == "exit":
        exit(0)
    roundNumber = roundNumber + 1
