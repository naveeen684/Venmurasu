from bs4 import BeautifulSoup
import tamil
from urllib.request import urlopen

old = "https://venmurasu.in/2014/01/01/%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AE%E0%AF%81%E0%AE%B0%E0%AE%9A%E0%AF%81-%E0%AE%A8%E0%AF%82%E0%AE%B2%E0%AF%8D-%E0%AE%92%E0%AE%A9%E0%AF%8D%E0%AE%B1%E0%AF%81/"
i = 0

while old:

    soup = BeautifulSoup(urlopen(old), "html.parser")
    body = soup.body.text
    words = []
    letters = tamil.utf8.get_letters(body)
    word = tamil.utf8.get_tamil_words(letters)

    for pos, word in enumerate(word):
        words.append(word)

    print(i, old)
    i += 1

    year = int(old[21:25])
    month = int(old[26:28])
    date = int(old[29:31])
    print(year, month, date)

    # save file
    with open("data/%s_%s_%s.txt" % (date, month, year), "w", encoding="utf-8") as f:
        for s in words:
            f.write(str(s) + "\n")

    # check whether the next blog is available or not
    try:
        new = soup.find('div', {'class': 'nav-next'})
        new = new.find('a')
        new = new.get('href')
        old = new
    except Exception as e:
        old = False
