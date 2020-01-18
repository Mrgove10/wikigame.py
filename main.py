from __future__ import print_function  # For Py2/3 compatibility
from yaspin.spinners import Spinners
from yaspin import yaspin
from wikipediaPage import wikipediaPage
import requests
import eel

urlStackTrace = []
language = "en"
randomArticleUrl = "https://"+language+".wikipedia.org/wiki/Special:Random"
baseArticleUrl = "https://"+language+".wikipedia.org/wiki/"
# initial pages
startPage = wikipediaPage(randomArticleUrl)
goalPage = wikipediaPage(randomArticleUrl)
urlStackTrace.append(startPage)

# Set web files folder
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def goToNextLink(idx):
    nextlink = urlStackTrace[-1].getOnlyLinksList()[idx]
    url = baseArticleUrl+nextlink
    print("going to ", url)
    urlStackTrace.append(wikipediaPage(url))
    eel.addRoundNumber()
    eel.updateRoundNumber()


@eel.expose
def goToPrevLink():
    old = urlStackTrace[-2].get('href')
    url = baseArticleUrl+nextlink
    print("going back to ", url)
    urlStackTrace.append(wikipediaPage(url))
    eel.addRoundNumber()
    eel.updateRoundNumber()


def printPath():
    print("This is the path you took :")
    for idx, val in enumerate(urlStackTrace):
        print(idx, ":", val.getTitle())


@eel.expose
def startGame():
    eel.updateRoundNumber()
    eel.updateStartPage([startPage.getTitle(), startPage.getUrl()])
    eel.updateGoalPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksList())


# Start the app
eel.start('index.html', mode='chrome-app')
