from __future__ import print_function  # For Py2/3 compatibility
from yaspin.spinners import Spinners
from yaspin import yaspin
from wikipediaPage import wikipediaPage
import requests
import eel

urlStackTrace = []
language = "en"
randomArticleUrl = "https://"+language+".wikipedia.org/wiki/Special:Random"
baseArticleUrl = "https://"+language+".wikipedia.org"
# initial pages
startPage = wikipediaPage(randomArticleUrl)
goalPage = wikipediaPage(randomArticleUrl)
urlStackTrace.append(startPage)

# Set web files folder
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def goToNextLink(int):
    print("goingto ", int)
    nextlink = urlStackTrace[-1].getAllLinksList()[int].get('href')
    url = baseArticleUrl+nextlink
    urlStackTrace.append(wikipediaPage(url))
    eel.addRoundNumber()


@eel.expose
def goToPrevLink():
    old = urlStackTrace[-2].get('href')
    url = baseArticleUrl+nextlink
    urlStackTrace.append(wikipediaPage(url))
    eel.addRoundNumber()


def printPath():
    print("This is the path you took :")
    for idx, val in enumerate(urlStackTrace):
        print(idx, ":", val.getTitle())


@eel.expose
def startGame():
    eel.updateRoundNumber(eel.getRoundNumber())
    eel.updateStartPage([startPage.getTitle(), startPage.getUrl()])
    eel.updateGoalPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksList())


# Start the app
eel.start('index.html', mode='chrome-app')
