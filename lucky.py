#! python3
#lucky.py - Otwiera kilka wyników wyszukiwania Google

import requests, sys, webbrowser, bs4

#print('Wyszukiwanie...')  #komunikat wyświetlany podczas pobierania strony Google
#res = requests.get('http://google.pl/search?q=' + ' '.join(sys.argv[1:]))
#res.raise_for_status()

# Pobieranie łączy z kilkoma pierwszymi wynikami wyszukiwania

#soup = bs4.BeautifulSoup(res.text, features="html.parser")
##print(soup)

## Otwieranie karty przeglądarki WWW dla każdego wyniku wyszukiwania

#linkElems = soup.select('.BNeawe a') # class BNeawe zawiera linki wyników, "a" oznacza <a>  </a> 
##print(linkElems)

#numOpen = min(5, len(linkElems))
#for i in range(numOpen):
#    webbrowser.open('http://google.pl' + linkElems[i].get('href'))

print('Wyszukiwanie...')  #komunikat wyświetlany podczas pobierania strony Allegro
allegroKategoria = ['wszystkie kategorie', 'dziecko', 'elektronika', 'firma', 'kolekcje i sztuka',
             'kultura i rozrywka', 'moda', 'motoryzacja', 'ogłoszenia i usługi', 'sport i turystyka', 
             'supermarket', 'uroda', 'zdrowie',
             ]
kategoria = ''

def checkKategoria(kategoria):
    """Funkcja zwraca kategorię z myślikami zamiast spacji"""
    print('Przesłano kategorię: '+ kategoria)
    if kategoria.lower() in allegroKategoria:
        return kategoria.replace(' ','-')
    else:
        print('Nieznana kategoria. Próbuję: ' + '"'+allegroKategoria[0] +'"')
        kategoria = ''
        return kategoria


if len(sys.argv) > 2:
    kategoria = checkKategoria(sys.argv[1].lower())
    if kategoria=='':
        allegroRes = requests.get('https://allegro.pl/listing?string='+' '.join(sys.argv[1:]))
    else:    
        allegroRes = requests.get('https://allegro.pl/kategoria/'+ kategoria.lower() + '?string='+' '.join(sys.argv[2:]))
else:
    allegroRes = requests.get('https://allegro.pl/listing?string='+' '.join(sys.argv[1:]))

allegroRes.raise_for_status()

# Pobieranie łączy z kilkoma pierwszymi wynikami wyszukiwania

soup = bs4.BeautifulSoup(allegroRes.text, features="html.parser")
#print(soup)

## Otwieranie karty przeglądarki WWW dla każdego wyniku wyszukiwania

linkElems = soup.select('._6713642 ') # class _6713642 zawiera linki wyników, "a" oznacza <a>  </a> 
#print(linkElems)

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://allegro.pl' + linkElems[i].get('href'))
