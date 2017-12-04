import urllib.request
from random import randint

''' 3EME METHODE: ON PREND LA PAGE QUE S'IL Y A LE MOT CLE DANS LE LIEN DE LA PAGE'''

'''
idees a implementer:
- eviter list de liens non pertinents (page d'acceuil, politique d'utilisation)
- eviter les boucles (ne pas repasser sur les liens deja visites)
'''
f = open('db3rdMethod.txt', 'w')

urlParcourt = "https://en.wikipedia.org/wiki/Computer"


def download_page(url):
    try:
        req = urllib.request.Request(url)
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
        end_quote = s.find('"', start_quote + 1)
        if (start_quote == -1) and (end_quote == 0):
            link = "0"
            return link, end_quote
        else:
            link = str(s[start_quote + 1:end_quote])
            return link, end_quote


def get_all_links(page, links, keyword):
    compteur = 0
    while True:
        link, end_link = get_next_link(page)
        if link == "0":
            break
        else:
            if link.find("wiki") != -1:
                if (link.find(".gif") == -1) and (
                        link.find(".png") == -1) and (
                        link.find(".svg") == -1) and (
                        link.find(".jpg") == -1) and (
                        link.find(":") == -1) and (
                        link.find(keyword) != -1):
                    links.append(link)
                    compteur += 1
                    if compteur >= 100:
                        break
                page = page[end_link:]
    return links


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
        return count
    except Exception as e:
        print(str(e))


def parcourt_links(page, keyword):
    # initial:
    print("Lien de depart: ", page)
    profondeur = int(input("choose depth: "))

    print("#########################")

    print("Lien de depart: ", page)
    print("#########################")
    print("")
    f.write("Lien de depart: ")
    f.write(str(page))
    f.write("\n")
    f.write("#############")
    f.write("\n")
    donnee = []
    d = download_page(page)
    get_all_links(d, donnee, keyword)

    # print("len: ", len(donnee))
    # avoidLinks = ['https://en.wikipedia.org/wiki/Main_Page']
    # successif:
    for i in range(profondeur):
        data2 = []
        rand = randint(1, len(donnee)-1)
        print(rand)
        print(len(donnee))

        print("profondeur", i + 1)

        if len(donnee) <= 2:
            print("pas assez de donnees")
            break
        else:
        
            next_link = "https://en.wikipedia.org" + donnee[rand]
            # print("#########################")
            # print("nouveau lien: ", nextLink)
            f.write(str(next_link))
            f.write("\n")
            print(pertinence(next_link, keyword, 0))
            f.write(str(pertinence(next_link, keyword, 0)))
            f.write("\n")
            print("############################")
            print(next_link)
            print("############################")
            d2 = download_page(next_link)
            donnee = get_all_links(d2, data2, keyword)

keyword = input("choose keyword: ")
parcourt_links(urlParcourt, keyword)
