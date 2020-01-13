import ui
from wikipediaPage import wikipediaPage
import requests 

game = True
roundNumber = 0
randomArticleURl = "https://en.wikipedia.org/wiki/Special:Random"

page1 = wikipediaPage(requests.get(randomArticleURl).url) 
#page2 = wikipediaPage(requests.get(randomArticleURl).url) 
print(page1.title.contents[0])
#print(page2.title.contents[0])

#entry point

#l = wikipediaPage("https://en.wikipedia.org/wiki/Tomorrowland_(festival)")
#print(l.title)
ui.startText()
page1.printLinkOptions()

while game :
    ui.roundText(roundNumber)
    # main loop
    choice = input("Your choice : ")
    
    roundNumber = roundNumber +1