import ui
from wikipediaPage import wikipediaPage
import requests
from yaspin import yaspin
from yaspin.spinners import Spinners

# varriable declarations
game = True
roundNumber = 1
randomArticleUrl = "https://en.wikipedia.org/wiki/Special:Random"
baseArticleUrl = "https://en.wikipedia.org"

urlStackTrace = []

ui.startText()
spinner = yaspin(Spinners.circleHalves, text="Loading...") #spinner
spinner.start()
# initial pages
startPage = wikipediaPage(randomArticleUrl)
goalPage = wikipediaPage(randomArticleUrl)
urlStackTrace.append(startPage)
spinner.stop()


def goToNextLink(currentpage, int):
    nextlink = currentpage.getAllLinksList()[int].get('href')
    url = baseArticleUrl+nextlink
    urlStackTrace.append(wikipediaPage(url))


while game:
    ui.roundText(roundNumber)
    print("Start page :", startPage.getTitle().contents[0], startPage.getUrl())
    print("Goal page :", goalPage.getTitle().contents[0], goalPage.getUrl())
    print("Current page :", urlStackTrace[-1].getTitle().contents[0], urlStackTrace[-1].getUrl())
    urlStackTrace[-1].printLinkOptions()
    choice = ""
    # main loop
    while choice == "":
        choice = input("Your choice : ")
        if choice == "exit":
            exit(0)
        spinner.start()
        goToNextLink(urlStackTrace[-1], int(choice))
    if goalPage.getUrl() == urlStackTrace[-1].getUrl() :
        print("victory")
        game = False
    roundNumber = roundNumber + 1
    spinner.stop()
