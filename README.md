## AjastinApp
Sovelluksen tarkoituksena on seurata töiden ja muiden projektien ajankäyttöä. Sovelluksessa on mahdollista luoda projekteja, joiden ajankäyttöä seurataan, seurata ajankäyttöä sovelluksen päänäkymässä olevalla ajastimella, sekä luoda projekteista käyttäjän määrittelemiä tulosteita, joista näkyy projektin ajankäyttöön liittyvää dataa.
## Dokumentaatio 
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Riippuvuuksien asentaminen: **poetry install**

2. Tietokannan alustaminen: **poetry run invoke build**

3. Ohjelman käynnistäminen: **poetry run invoke start**. Ohjelmaan voi kirjautua testitunnuksilla: username "Test", password "secret"

## Komentorivitoiminnot

Ohjelman käynnistäminen: **poetry run invoke start** 

Testien suoritus: **poetry run invoke test**

Testikattavuusraportin generointi: **poetry run invoke coverage-report** Raportti generoituu gitignorattuun ./_htmlcov_-hakemistoon.

pylint raportti: **poetry run invoke lint**

