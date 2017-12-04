import urllib.request
from random import randint


urlParcourt = "https://en.wikipedia.org/wiki/Flip_(form)"
count = 0
word = "computer"

def pertinence(url, keyword, count):
    count = 0
    liste = []
    try:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read().decode().split())
        count = respData.count(keyword)
        totalMots = respData.count(" ")
        print(count, "occurences du mot ", keyword, "pour la page: ", urlParcourt, "sur: ", totalMots, "mots au total")
    except Exception as e:
        print(str(e))


pertinence(urlParcourt, word, count)