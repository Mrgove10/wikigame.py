# wikigame.py

wikigame.py is a simple python game to learn tons of stuff on wikipedia.

You are given two random pages, one is where you start, the over is where you need to go.
Try to get to the second page in the less moves possible.

Warning : This game can be very hard. There are more then 6 000 000 (Jan 2020) articles on the english wikipedia website. And the articles are choosen at random ... Good luck, you will need it.

## To install

```bash
pip install -r requirements.txt
```

### Used libraries

- [requests](https://github.com/psf/requests)
- [beautifulsoup4](https://github.com/wention/BeautifulSoup4)
- [urllib3](https://github.com/urllib3/urllib3)
- [eel](https://github.com/samuelhwilliams/Eel)

## To play

```bash
python main.py
```

once lanched, the game should open a new tab in your browser.

## Tested on

|OS|Browser|Works|
|---|---|---|
|Windows|Firefox|✅|
|Linux|Firefox|❌|