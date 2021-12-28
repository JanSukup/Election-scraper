import sys
from bs4 import BeautifulSoup
import requests
import csv

def ziskani_vstupu():
    vstup = sys.argv
    if len(vstup) != 3:
        print("Chybné zadání. Ukončuji.")
        quit()
    if "https://volby.cz/pls/ps2017nss/" not in vstup[1]:
        print("První argument musí obsahovat internetovou adresu. Ukončuji.")
        quit()
    if ".csv" != vstup[2][-4:len(vstup[2])]:
        print("Chybný vstup. Druhý argument musí obsahovat jméno souboru pro výstup, včetně koncovky .csv. Ukončuji.")
    return vstup

def seznam_obci(zadani_uzivatele: list):
    getr = requests.get(zadani_uzivatele[1])
    soup = BeautifulSoup(getr.text, 'html.parser')
    vysledek = [["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy" ]]
    pomocny_list = []
    seznam_linku = ziskani_vysledku_obce(soup)
    for text in soup.find_all("td"):
        if len(text.text) < 2:
            continue
        if len(pomocny_list) >= 1:
            pomocny_list.append(text.text)
#            pomocny_list.append(ziskani_vysledku_obce(pomocny_list[1]))
            vysledek.append(pomocny_list)
            pomocny_list = []
        else:
            pomocny_list.append(text.text)
    vysledek.append(seznam_linku)
    print("Stahuji data z", zadani_uzivatele[1])
    return vysledek


def ziskani_vysledku_obce(soup):
    seznam_linku = []
    for link in soup.select("td.cislo a"):
        seznam_linku.append("https://volby.cz/pls/ps2017nss/" + link["href"])
    return seznam_linku

def strany(prvni_strana:str):
    getr = requests.get(prvni_strana)
    soup = BeautifulSoup(getr.text, 'html.parser')
    seznam_stran = []
    for strana in soup.select("td.overflow_name"):
        seznam_stran.append(strana.text)
    return seznam_stran

def vysledek_obce(link_vysledku:str):
    getr = requests.get(link_vysledku)
    soup = BeautifulSoup(getr.text, 'html.parser')
    vysledek = []
    vysledek.append(soup.find("td", headers="sa2").text.replace("\xa0", ""))
    vysledek.append(soup.find("td", headers="sa3").text.replace("\xa0", ""))
    vysledek.append(soup.find("td", headers="sa6").text.replace("\xa0", ""))
    for polozka in soup.find_all(headers="t1sa2 t1sb3" or "t2sa2 t2sb3"):
        if "\xa0" in polozka.text:
            vysledek.append(polozka.text.replace("\xa0", ""))
        else:
            vysledek.append(polozka.text)
    for polozka in soup.find_all(headers="t2sa2 t2sb3"):
        if "\xa0" in polozka.text:
            vysledek.append(polozka.text.replace("\xa0", ""))
        elif polozka.text != "-":
            vysledek.append(polozka.text)
    print("Stahuji výsledek obce z", link_vysledku)
    return vysledek

def csv_export(exportovany_list: list, jmeno_souboru: str):
    with open(jmeno_souboru, "w", newline="") as csv_soubor:
        writer = csv.writer(csv_soubor)
        for radek in exportovany_list:
            writer.writerow(radek)
    print("Ukládám soubor", jmeno_souboru)

def hlavni():
    vstup = ziskani_vstupu()
    vysledek = seznam_obci(vstup)
    seznam_stran = strany(vysledek[-1][1])
    for strana in seznam_stran:
        vysledek[0].append(strana)
    vysledek_obce_pomocny = []
    for index_obce,link in enumerate(vysledek[-1]):
        vysledek_obce_pomocny = vysledek_obce(link)

        for vysledek_strany in vysledek_obce_pomocny:
            vysledek[index_obce+1].append(vysledek_strany)
    vysledek.pop(-1)
    csv_export(vysledek,vstup[2])





if __name__ == "__main__":
    hlavni()





