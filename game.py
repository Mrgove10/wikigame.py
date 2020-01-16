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

def startGame():
    ui.startText()
    spinner = yaspin(Spinners.circleHalves, text="Loading...")  # spinner
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


def goToPrevLink():
    old = urlStackTrace[-2].get('href')
    url = baseArticleUrl+nextlink
    urlStackTrace.append(wikipediaPage(url))


def printPath():
    print("This is the path you took :")
    for idx, val in enumerate(urlStackTrace):
        print(idx, ":", val.getTitle())


while game:
    ui.roundText(roundNumber)
    print("Start page :", startPage.getTitle(), startPage.getUrl())
    print("---")
    print("Goal page :", goalPage.getTitle(), goalPage.getUrl())
    print("---")
    print("Current page :",
          urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl())
    print("---")
    urlStackTrace[-1].printFirstTenLinkOptions()
    print("-1 : to show all links")
    print("back : goes back one step")
    # try:
    nextLink = False
    while not nextLink:
        choice = input("Your choice : ")
        if choice == "-1":
            urlStackTrace[-1].printLinkOptions()
        elif choice == "exit":
            printPath()
            game = False
            exit(0)
        elif choice == "back":
            goToPrevLink()
        elif choice == "":
            pass
        elif 0 <= int(choice) <= len(urlStackTrace[-1].getAllLinksList()):
            spinner.start()
            goToNextLink(urlStackTrace[-1], int(choice))
            nextLink = True
    # except:
    #     print("An error has occured")
    if goalPage.getUrl() == urlStackTrace[-1].getUrl():
        print("victory in", roundNumber, "steps")
        printPath()
        game = False
    roundNumber = roundNumber + 1
    spinner.stop()