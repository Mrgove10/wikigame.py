from __future__ import print_function  # For Py2/3 compatibility
from yaspin.spinners import Spinners
from yaspin import yaspin
from wikipediaPage import wikipediaPage
import requests
import eel

# game = vars()
urlStackTrace = []
roundNumber = None
language = None
randomArticleUrl = None
baseArticleUrl = None


# Set web files folder
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def goToNextLink(int):
    print("goingto ", int)
    nextlink = urlStackTrace[-1].getAllLinksList()[int].get('href')
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


def startGame():
    eel.updateRoundNumber(roundNumber)
    eel.updateStartPage([startPage.getTitle(), startPage.getUrl()])
    eel.updateGoalPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksList())

    try:
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
                goToNextLink(int(choice))
                nextLink = True
    except:
        print("An error has occured")
    if goalPage.getUrl() == urlStackTrace[-1].getUrl():
        printPath()
        game = False
    roundNumber = roundNumber + 1

@eel.expose
def setUp():
    urlStackTrace = []
    roundNumber = 1
    language = "en"
    randomArticleUrl = "https://"+language+".wikipedia.org/wiki/Special:Random"
    baseArticleUrl = "https://"+language+".wikipedia.org"
    # initial pages
    startPage = wikipediaPage(randomArticleUrl)
    goalPage = wikipediaPage(randomArticleUrl)
    urlStackTrace.append(startPage)
    print(type(roundNumber))
    startGame()


setUp()

# Start the app
eel.start('index.html', mode='chrome-app')
