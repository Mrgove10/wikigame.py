from bs4 import BeautifulSoup
import urllib.request
import sys
import ui
from wikipediaPage import wikipediaPage

randomArticleURl = "https://en.wikipedia.org/wiki/Special:Random"

#entry point
ui.startText()
l = wikipediaPage("https://en.wikipedia.org/wiki/Tomorrowland_(festival)")
print(l.title)
