import time
import urllib.request
import re
from random import randint

starting_page = "https://en.wikipedia.org/wiki/Math"
seed_page = "https://en.wikipedia.org"  #Crawling the English Wikipedia

urlParcourt = "https://en.wikipedia.org/wiki/Computer"

def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        print(str(e))

def get_next_link(s):
    start_link = s.find("<a href")
    if start_link == -1:
        end_quote = 0
        link = "0"
        return link, end_quote
    else:
        start_quote = s.find('"/wiki', start_link)
        end_quote = s.find('"',start_quote+1)
        if (start_quote == -1) and (end_quote == 0):
            link = "0"
            return link, end_quote
        else:
            link = str(s[start_quote+1:end_quote])
            return link, end_quote

def get_all_links(page, links=[]):
    compteur = 0
    while True:
        link, end_link = get_next_link(page)
        if link == "0":
            break
        else:
            if link.find("wiki") != -1:
                if (link.find(".gif") == -1) and (link.find(".png") == -1) and (link.find(".svg") == -1) and (link.find(".jpg") == -1) and (link.find(":") == -1):
                    links.append(link)
                    compteur+=1
                    if compteur >= 50:
                        break
                page = page[end_link:]
    return links


def parcourt(page):
    # initial:
    print("#########################")
    print("Lien de depart: ", page)
    print("#########################")
    print("")
    donnee = []
    d = download_page(page)
    get_all_links(d, donnee)

    # successif:
    for i in range(100):
        data2 = []
        rand = randint(1,9)
        print(rand)
        nextLink = "https://en.wikipedia.org"+donnee[rand]
        print("#########################")
        print("nouveau lien: ", nextLink)
        #print("#########################")
        d2 = download_page(nextLink)
        donnee = get_all_links(d2, data2)

parcourt(urlParcourt)