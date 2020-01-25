from __future__ import print_function  # For Py2/3 compatibility
from wikipediaPage import wikipediaPage
import eel
import time

#Variables
wikiPageStackTrace = []  # List of the wikipedia objects
titleStackTrace = []  # list of the title of the pages
urlStackTrace = []
language = "en"
baseArticleUrl = "https://"+language+".wikipedia.org"
randomArticleUrl = baseArticleUrl+"/wiki/Special:Random"
testArticleOne = baseArticleUrl+"/wiki/Apple_Inc."
testArticleTwo = baseArticleUrl+"/wiki/IPhone"

# initial pages
startPage = wikipediaPage(testArticleOne)
goalPage = wikipediaPage(testArticleTwo)
wikiPageStackTrace.append(startPage)
titleStackTrace.append(startPage.getTitle())
urlStackTrace.append(startPage.getUrl())

eel.init('web', allowed_extensions=['.js', '.html'])# Set web files folder

@eel.expose
def goToNextLink(idx):
    """
    Goes the the next page depending of what index of the link is on the page
    """
    eel.showLoader()
    nextlink = wikiPageStackTrace[-1].getRawList()[idx].get('href')
    url = baseArticleUrl+nextlink
    print("going to ", url)
    newpage = wikipediaPage(url)
    wikiPageStackTrace.append(newpage)
    titleStackTrace.append(newpage.getTitle())
    urlStackTrace.append(newpage.getUrl())
    update()


@eel.expose
def goToPrevLink():
    """
    Goes back one page in the history
    """
    eel.showLoader()
    if wikiPageStackTrace[-2].getUrl() != "":
        oldpage = wikiPageStackTrace[-2]
        print("going back to ", oldpage.getUrl())
        titleStackTrace.append(oldpage.getTitle())
        urlStackTrace.append(oldpage.getUrl())
        del wikiPageStackTrace[-1]
        update()
    else:
        update()


def update():
    """
    lanches all the things we do in between pages
    """
    print("current page is ", wikiPageStackTrace[-1].getTitle())
    if not checkIfVictory(urlStackTrace[-1], goalPage.getUrl()):
        eel.addRoundNumber()
        eel.printInPageList(wikiPageStackTrace[-1].getOnlyLinksListJS())
        eel.updateCurrentPage(
            [wikiPageStackTrace[-1].getTitle(), wikiPageStackTrace[-1].getUrl()])
        eel.updateCurrentPageDescription(wikiPageStackTrace[-1].getFirstSentence())
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


def checkIfVictory(urlCurrentPage, urlGoalPage):
    """
    Checks for victory
    """
    if urlCurrentPage == urlGoalPage:
        print("Victory ! ")
        return true
    eel.showvictory()


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
        [wikiPageStackTrace[-1].getTitle(), wikiPageStackTrace[-1].getUrl()])
    eel.updateCurrentPageDescription(wikiPageStackTrace[-1].getFirstSentence())

    eel.printInPageList(wikiPageStackTrace[-1].getOnlyLinksListJS())
    eel.hideLoader()


# Start the app
eel.start('index.html', mode='chrome-app')
