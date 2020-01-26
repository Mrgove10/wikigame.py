# wikigame.py

wikigame.py is a simple python game to learn tons of stuff on wikipedia.

You are given two random pages, one is where you start, the over is where you need to go.
Try to get to the second page in the less moves possible.

Warning : This game can be very hard. There are more then 6 000 000 (Jan 2020) articles on the english wikipedia website. And the articles are choosen at random ... Good luck, you will need it.

Please use **python 3**

## General Info

Sometimes you can see "null" as an option, those links can still be clicked. And you know what they say "its not a bug its a feature", just makes the game harder.

## To install

```bash
pip3 install -r requirements.txt
```

### Main libraries used

- [beautifulsoup4](https://github.com/wention/BeautifulSoup4)
- [eel](https://github.com/samuelhwilliams/Eel)

## To play

```bash
python3 main.py
```

Once lanched, the game should open a new tab in your browser.
If the page does not open automagicly you can go to http://localhost:8000/index.html on your browser

## Tested on

| OS              | Browser | Python Version | Works |
| --------------- | ------- | -------------- | ----- |
| Windows         | Firefox | 3.6.8          | ✅     |
| Linux (Pop!_OS) | Firefox | 3.7.3          | ✅     |

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)