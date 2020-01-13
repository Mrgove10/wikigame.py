import ui
from wikipediaPage import wikipediaPage
import requests

# varriable declarations
game = True
roundNumber = 1
randomArticleUrl = "https://en.wikipedia.org/wiki/Special:Random"
baseArticleUrl = "https://en.wikipedia.org/"

urlStackTrace = []

#initial pages
startPage = wikipediaPage(randomArticleUrl)
goalPage = wikipediaPage(randomArticleUrl)
currentpage = startPage # only for the start

urlStackTrace.append(startPage)
print(urlStackTrace)

ui.startText()

def goToNextLink(currentpage, int):
    print("Going to next page")
    nextlink = currentpage.allLinksList[int].get('href')
    url = baseArticleUrl+nextlink
    currentpage = wikipediaPage(url)

while game:
    ui.roundText(roundNumber)
    print("Start page :", startPage.title.contents[0])
    print("Goal page :", goalPage.title.contents[0])
    print("Current page :", currentpage.title.contents[0])
    currentpage.printLinkOptions()
    choice = ""
    # main loop
    while choice == "":
        choice = input("Your choice : ")
        goToNextLink(currentpage, int(choice))
        if choice == "exit":
            exit(0)
    roundNumber = roundNumber + 1
