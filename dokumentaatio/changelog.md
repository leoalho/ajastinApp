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
- Siirretty ajastimen toiminnallisuus MainView-luokasta TimerService-luokkaan
- Luotu käyttäjien toiminnallisuutta varten oma luokka: UserService
- Laajennettu ajastimen toiminnallisuutta: sekuntien sijaan näkyy sekunnit, minuutit ja tunnit
- Lisätty projektinäkymä, joka mahdollistaa jo luoduita projekteista projektin valinnan
- Otettu ympäristömuuttujat käyttöön .env-kansioon
- Aloitettu lintaus
