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
print("startPage", startPage.getUrl())
goalPage = wikipediaPage(randomArticleUrl)
print("goalPage", goalPage.getUrl())
urlStackTrace.append(startPage)
startPage.printLinkNamesConsole()
# Set web files folder
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def goToNextLink(idx):
    nextlink = urlStackTrace[-1].getRawList()[idx].get('href')
    url = baseArticleUrl+nextlink
    print("going to ", url)
    urlStackTrace.append(wikipediaPage(url))
    update()


@eel.expose
def goToPrevLink():
    old = urlStackTrace[-2].getRawList().get('href')
    url = baseArticleUrl+old
    print("going back to ", url)
    urlStackTrace.append(wikipediaPage(url))
    update()

def update():
    eel.addRoundNumber()
    eel.clearPageList()
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())
    eel.updateCurrentPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateRoundNumber()

# todo implement in the web page
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
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())
    

# Start the app
eel.start('index.html', mode='chrome-app')
