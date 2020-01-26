# wikigame.py

wikigame.py is a simple python game to learn tons of stuff on wikipedia.

You are given two random pages, one is where you start, the over is where you need to go.
Try to get to the second page in the less moves possible.

Warning : This game can be very hard. There are more then 6 000 000 (Jan 2020) articles on the english wikipedia website. And the articles are choosen at random ... Good luck, you will need it.

## To install

To run please use **python 3**

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