from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import sys

class wikipediaPage():
    def __init__(self, url):
        """
        init methode
        """
        self.__url = url
        self.__title = ""
        self.__rawPageContent = ""
        self.__allLinksList = []
        # calls the needed methodes
        self.getRawPageContent()
        self.getAllLinksInPage()
        self.getPageTitle()

    def getRawPageContent(self):
        """
        Gets the raw content of the page
        """
        req = Request(
            url=self.__url,
            headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        handler = urlopen(req)
        with handler as response:
            soup = BeautifulSoup(response, 'html.parser')
            self.__rawPageContent = soup
            self.__url = handler.geturl()  # sets the correct adress

    def getAllLinksInPage(self):
        """
        uses beautifusoup to retreive all the links in a page
        """
        soup = self.__rawPageContent
        # selects all the pragraphs
        for x in soup.find_all(True, {'class': [
            'IPA', 'external text', 
            'external', 'internal', 
            'citation book', 'plainlinks', 
            'nowrap', 'portal', 'image',
            'navbox', 'infobox_v3', 
            'infobox_v2', 'infobox'
            ]}):
            x.decompose()
        for x in soup.find_all(True, {'id': [
            'footer', 'toc',
            'mw-panel', 'mw-head',
            'catlinks'
            ]}):
            x.decompose()
        # all paragraphs
        all_links = soup.select('p a[href^="/wiki"]')
        # seests all the table
        all_links.extend(soup.select('table[class^="wikitable"] a[href^="/wiki"]'))
        # ul lists
        all_links.extend(soup.select('ul a[href^="/wiki"]'))
        # ol lists
        all_links.extend(soup.select('ol a[href^="/wiki"]'))
        for idx, val in enumerate(all_links):#remouves all the "null" titles. TOOD : maney don't leave this in
            if(val.contents[0] == ""):
                del all_links[-1]
    
        self.__allLinksList = all_links

    def getPageTitle(self):
        """
        Gets the page title of the page as a string
        """
        temp = str(self.__rawPageContent.find('h1').contents[0])
        temp = temp.replace('<i>', '')
        temp = temp.replace('</i>', '')
        self.__title = temp

    def getFirstSentence(self):
        """
        Gets the firsqt sentence of the page
        """
        text = self.__rawPageContent.find(
            'p', attrs={'class': None}).get_text()
        text = text.partition('.')[0] + '.'
        return text

    def printLinkNamesConsole(self):
        """
        Print in the console all the link options
        """
        for idx, val in enumerate(self.__allLinksList):
            print(idx, ":", val.contents[0])

    def printFirstTenLinkNamesConsole(self):
        """
        Print in the console the 10 first link names
        """
        if len(self.__allLinksList) > 10:
            for i in range(10):
                print(i, ":", self.__allLinksList[i].contents[0])
        else:
            self.printLinkNamesConsole()

    def getTitle(self):
        """
        use getPageTitle() insteed
        """
        return self.__title

    def getOnlyLinksListJS(self):
        """
        returns the links as a list
        used in JS side
        """
        temp = []
        for idx, val in enumerate(self.__allLinksList):
            temp.append(val.contents[0])
        return temp

    def getUrl(self):
        """
        gets the page url
        """
        return self.__url

    def getRawList(self):
        """
        gets the page url
        """
        return self.__allLinksList
