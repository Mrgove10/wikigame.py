from bs4 import BeautifulSoup
import urllib.request
import sys


class wikipediaPage():
    def __init__(self, url=""):
        self.url = url
        self.title = ""
        self.rawpageContent = ""
        self.allLinksList = []
        # calls the needed methodes
        self.getRawPageContent()
        self.getAllLinks()
        self.getPageTitle()

    def getRawPageContent(self):
        req = urllib.request.Request(
            url="https://en.wikipedia.org/wiki/Python_(programming_language)",
            headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        handler = urllib.request.urlopen(req)
        with handler as response:
            soup = BeautifulSoup(response, 'html.parser')
            self.rawpageContent = soup

    def getAllLinks(self):
        soup = self.rawpageContent
        # selects all the pragraphs
        for x in soup.find_all(True, {'class': ['external', 'internal', 'nowrap', 'image', 'navbox', 'infobox_v3', 'infobox_v2', 'infobox_v1', 'infobox']}):
            x.decompose()
        for x in soup.find_all(True, {'id': ['toc', 'mw-panel', 'catlinks']}):
            x.decompose()
        all_links = soup.select('p a[href^="/wiki"]')
        # seests all the table
        all_links.extend(soup.select(
            'table[class^="wikitable"] a[href^="/wiki"]'))

        all_links.extend(soup.select('ul a[href^="/wiki"]'))
        all_links.extend(soup.select('ol a[href^="/wiki"]'))
        self.allLinksList = all_links
        # for p in all_links:
        #     allLinksList.append(p)
        #     print(p)
        # print(len(all_links))

    def getPageTitle(self):
        self.title = self.rawpageContent.find('h1')

    def printLinkOptions(self):
        for p in self.allLinksList:
            print(p.contents[0])
