# Changelog

## Viikko 3 
- Luotu graafinen käyttöliitymä ja tähän liittyen LoginView ja mainView -luokat
- Luotu User luokka
- Luotu TimerService luokka, joka yhdistää tietokantaan, initialisoi käyttäjätaulun ja vastaa kirjautumislogiikasta.
- Käyttäjä voi kirjautua sisään tietokannan testikäyttäjällä (nimi: "Test")
- Käyttäjä voi kirjautumisen jälkeen ottaa aikaa yksinkertaisella sekuntikellolla. Ajanoton arvoja ei vielä tallenneta tietokantaan.
- Luotu Invoke-taskit ohjelman käynnistämiselle, testaamiselle, ja coverage-reporttia varten
- Luotu yksittäinen yksinkertainen testi käyttäjäluokalle

## Viikko 4
- Refaktoroitu database repository-mallin mukaisesti
- Siirretty ajastimen toiminnallisuus MainView-luokasta omaan Timer-luokkaan
- Laajennettu ajastimen toiminnallisuutta: sekuntien sijaan näkyvät sekunnit, minuutit ja tunnit
- Lisätty projektinäkymä, joka mahdollistaa jo luoduista projekteista projektin valinnan
- Laaditu omat näkymät ja toiminnallisuus uusien projektien ja käyttäjien luomiseksi
- Lisätty näkymät ja toiminnallisuus käyttäjien ja projektien lisäämiseksi
- Lisätty mahdollisuus uloskirjautumiseen sekä projektien vaihtamiseen
- Mahdollista exportaa projektin ajanotot/vuorokausi. Exportit tulevat juurihakemistossa olevaan exports hakemistoon
- Otettu ympäristömuuttujat käyttöön .env-kansioon
- Lisätty uusi taski tietokannan alustamista varten
- Aloitettu lintaus Pylintilla
- Laajennettu testejä

## Viikko 5
- Lisätty salasana kirjautumisnäkymään
- Salasanan vaatiminen käyttäjän luonnin yhteydessä, testikäyttäjä: käyttäjätunnus: "Test", salasana "secret"
- Salasanan hashaus bcrypt kirjaston avulla
- Lisätty messageBoxit virheellisille inputeille käyttäjän ja projektin luonnin sekä sisäänkirjautumisen yhteydessä
- Laajennettu testikattavuutta
