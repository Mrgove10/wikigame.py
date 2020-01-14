from bs4 import BeautifulSoup
import urllib.request
import sys
from yaspin import yaspin

class wikipediaPage():
    def __init__(self, url):
        self.__url = url
        self.__title = ""
        self.__rawPageContent = ""
        self.__allLinksList = []
        # calls the needed methodes
        self.getRawPageContent()
        self.getAllLinks()
        self.getPageTitle()

    def getRawPageContent(self):
        req = urllib.request.Request(
            url=self.__url,
            headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        handler = urllib.request.urlopen(req)
        with handler as response:
            soup = BeautifulSoup(response, 'html.parser')
            self.__rawPageContent = soup
            self.__url = handler.geturl()  # sets the correct adress

    def getAllLinks(self):
        soup = self.__rawPageContent
        # selects all the pragraphs
        for x in soup.find_all(True, {'class': ['IPA', 'external', 'internal', 'citation book', 'plainlinks', 'nowrap', 'portal', 'image', 'navbox', 'infobox_v3', 'infobox_v2', 'infobox']}):
            x.decompose()
        for x in soup.find_all(True, {'id': ['footer', 'toc', 'mw-panel', 'mw-head', 'catlinks']}):
            x.decompose()
        # all paragraphs
        all_links = soup.select('p a[href^="/wiki"]')
        # seests all the table
        all_links.extend(soup.select(
            'table[class^="wikitable"] a[href^="/wiki"]'))
        # ul lists
        all_links.extend(soup.select('ul a[href^="/wiki"]'))
        # ol lists
        all_links.extend(soup.select('ol a[href^="/wiki"]'))
        self.__allLinksList = all_links

    def getPageTitle(self):
        self.__title = self.__rawPageContent.find('h1')

    def printLinkOptions(self):
        for idx, val in enumerate(self.__allLinksList):
            print(idx, ":", val.contents[0])

    def printFirstTenLinkOptions(self):
        if len(self.__allLinksList) > 10:
            for i in range(10):
                print(i, ":", self.__allLinksList[i].contents[0])
        else:
            self.printLinkOptions()

    def getTitle(self):
        return self.__title.contents[0]

    def getAllLinksList(self):
        return self.__allLinksList

    def getUrl(self):
        return self.__url
