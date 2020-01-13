from bs4 import BeautifulSoup
import urllib.request
import sys

callStack = []

randomArticleURl = "https://en.wikipedia.org/wiki/Special:Random"

def score(listresult):
    total = 0
    listresult.sort(reverse=True)
    for t in listresult:
        total += t
    percent = listresult[0] / total
    print(percent*100)


def search():
    req = urllib.request.Request(
        url="https://en.wikipedia.org/wiki/Chelsea_McClammer",
        headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    handler = urllib.request.urlopen(req)
    with handler as response:
        soup = BeautifulSoup(response, 'html.parser')
        for resultStats in soup.find_all("a"):
            print(resultStats)
            
            
            
            
print("bonjour")
search()