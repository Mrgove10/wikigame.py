from __future__ import print_function  # For Py2/3 compatibility
from yaspin.spinners import Spinners
from yaspin import yaspin
from wikipediaPage import wikipediaPage
import requests
import eel
import time

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
    """
    Goes the the next page depending of what index of the link is on the page
    """
    eel.showLoader()
    nextlink = urlStackTrace[-1].getRawList()[idx].get('href')
    url = baseArticleUrl+nextlink
    print("going to ", url)
    urlStackTrace.append(wikipediaPage(url))
    update()


@eel.expose
def goToPrevLink():
    """
    Goes back one page in the history
    """
    eel.showLoader()
    print(len(urlStackTrace))
    if len(urlStackTrace) == 2:
        old = urlStackTrace[-1].getUrl()
    else:
        old = urlStackTrace[-2].getUrl()
    print("going back to ", old)
    urlStackTrace.append(wikipediaPage(old))
    update()

def update():
    """
    lanches all the things we do in between pages
    """
    eel.addRoundNumber()
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())
    eel.updateCurrentPage([urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.updateRoundNumber()
    eel.updateHistory(getHistory())
    time.sleep(0.25) #we need to do this because overwise the JS is not fat egoth to respond so we get an infinit loading 
    eel.hideLoader()
    
def getHistory():
    """
    Gets the history of the pages the user has visited
    """
    temp = []
    for idx, val in enumerate(urlStackTrace):
        temp.append(val.getTitle())
    return temp

@eel.expose
def startGame():
    """
    function used to launch the game
    """
    eel.updateRoundNumber()
    eel.updateStartPage([startPage.getTitle(), startPage.getUrl()])
    eel.updateGoalPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())

# Start the app
eel.start('index.html', mode='chrome-app')
