from __future__ import print_function  # For Py2/3 compatibility
from yaspin.spinners import Spinners
from yaspin import yaspin
from wikipediaPage import wikipediaPage
import requests
import eel
import time

urlStackTrace = []  # List of the urls
titleStackTrace = []  # list of the title of the pages
language = "en"
randomArticleUrl = "https://"+language+".wikipedia.org/wiki/Special:Random"
baseArticleUrl = "https://"+language+".wikipedia.org"
# initial pages
startPage = wikipediaPage(randomArticleUrl)
goalPage = wikipediaPage(randomArticleUrl)
urlStackTrace.append(startPage)
titleStackTrace.append(startPage.getTitle())
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
    newpage = wikipediaPage(url)
    urlStackTrace.append(newpage)
    titleStackTrace.append(newpage.getTitle())
    update()


@eel.expose
def goToPrevLink():
    """
    Goes back one page in the history
    """
    eel.showLoader()
    if urlStackTrace[-2] != null:
        oldpage = urlStackTrace[-2]
        print("going back to ", oldpage.getUrl())
        titleStackTrace.append(oldpage.getTitle())
        del urlStackTrace[-1]
        update()
    else:
        update()


def update():
    """
    lanches all the things we do in between pages
    """
    eel.addRoundNumber()
    print("current page is ", urlStackTrace[-1].getTitle())
    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())
    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.updateCurrentPageDescription(urlStackTrace[-1].getFirstSentence())
    eel.updateRoundNumber()
    eel.updateHistory(getHistoryTitles())
    # we need to do this because overwise the JS is not fat egoth to respond so we get an infinit loading
    time.sleep(0.5)
    eel.hideLoader()


def getHistoryTitles():
    """
    Gets the history of the pages the user has visited
    """
    temp = []
    for idx, val in enumerate(titleStackTrace):
        temp.append(val)
    return temp


@eel.expose
def startGame():
    """
    function used to launch the game
    """
    eel.updateRoundNumber()

    eel.updateStartPage([startPage.getTitle(), startPage.getUrl()])
    eel.updateStartPageDescription(startPage.getFirstSentence())

    eel.updateGoalPage([goalPage.getTitle(), goalPage.getUrl()])
    eel.updateGoalPageDescription(goalPage.getFirstSentence())

    eel.updateCurrentPage(
        [urlStackTrace[-1].getTitle(), urlStackTrace[-1].getUrl()])
    eel.updateCurrentPageDescription(urlStackTrace[-1].getFirstSentence())

    eel.printInPageList(urlStackTrace[-1].getOnlyLinksListJS())


# Start the app
eel.start('index.html', mode='chrome-app')
