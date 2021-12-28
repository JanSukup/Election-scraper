# Election-scraper


## Popis projektu
Tento projekt stahuje výsledky parlamentních voleb z roky 2017. 

## Instalace knihoven
Potřebné knihovny jsou vypsané v souboru reqirements.txt, který je součástí projektu. 
```
$ pip3 --version
$ pip3 install -r requirements.txt
```
## Souštění projektu
Projekt je nutné spouštět z příkazového řádku. Spuštění vyžaduje dva argumenty. První argument je link na volební výsledky daného územního celku (okresu). Druhý argument je název generovaného souboru včetně přípony `.csv`. 
```
election_scraper.py <odkaz na stránku územního celku> <název výstupního souboru>
```
## Ukázka projektu
Výběr okresu lze provádět na stránce `https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ` kliknutím na X ve sloupci "Výběr obce".

1. argument `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6204`
2. argument `breclav.csv`

Kompletní zpuštění projektu:
```
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6204" "breclav.csv"
```
## Ukázka běhu 
Script v terminálu vypisuje průběh stahování
```
Stahuji data z  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
Stahuji výsledek obce z  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103
Stahuji výsledek obce z  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=589268&xvyber=7103
...
Stahuji výsledek obce z  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=590240&xvyber=7103
Ukládám soubor  prostejov.csv
Ukončuji election_scraper
```
Částečná ukázka výstupu:
```
kód obce,název obce,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,...
584304,Bavory,334,236,236,42,0,0,10,0,10,22,6,6,4,0,0,20,0,14,66,1,0,15,0,0,0,1,18,0,1
584321,Boleradice,737,487,483,47,3,1,25,2,28,31,4,7,7,1,1,30,0,18,145,2,1,72,0,0,3,4,46,2,3
...
```


