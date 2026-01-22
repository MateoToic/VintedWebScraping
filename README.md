# VintedWebScraping
Projekt demonstrira web scraping stranice vinted s ciljem daljnjeg provođenja strojnog učenja nad podacima.
Korištena su dva pristupa:
1) HTML scraping (Playwright)
2) API scraping
Prikupljeni podaci će se kasnije koristiti u drugom projektu u kojem će se nad njima provoditi razni algoritmi strojnog učenja u svrhu predikcije isplativosti prodaje pojedinih artikala. Podaci, odnosno pristup njihovom dobivanju, primarno su fokusirani na tenisice, no projekt je dizajniran skalabilno, što omogućuje jednostavnu prilagodbu za prikupljanje podataka o drugim vrstama artikala.

1) HTML scraping uz Playwright
Scraping se provodi simulirajući stvarnog korisnika koji navigira kroz web stranicu pomoću Playwrighta.
Renderira se svaka web stranica, čita podatke iz HTML DOM-a te se omogućuje interakcija sa stranicom.

Sporiji i nesigurniji izbor, u idealnoj situaciji se koristi kao fallback ukoliko API scrapanje nije moguće, no u ovom projektu napravljeno zasebno.

Prikupljeni podaci:
- Id artikla
- Stanje artikla
- Cijena
- Broj favorita
- Veličina

--------------------------------------------------------------------

2) API scraping
Umjesto parsiranja samog HTML-a, koriste se interni API pozivi koje frontend poziva u pozadini.
Za analizu i testiranje internih API poziva korišten je alat Insomnia, koji je omogućio jednostavan pregled HTTP zahtjeva i odgovora te lakše razumijevanje strukture podataka koje frontend koristi.
