# Käyttöohje

Viimeisin [release](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases). Lataa releasen lähdekoodi Assetsien alla olevasta source codesta

## Käynnistäminen

Ennen käynnistämistä asenna riippuvuuden komennolla **poetry install**

Tämän jälkeen alusta tietokanta komennolla **poetry run invoke build**

Ohjelma käynnistetään komennolla **poetry run invoke start**

## Kirjautuminen

Kirjautuminen tapahtuu kirjoittamalla käyttäjätunnus ja salasanat niitä vastaaviin kenttiin ja painamalla login painiketta. Sovelluksessa on tietokannan alustuksen yhteydessä luotu oletuskäyttäjä käyttäjänimellä "Test" ja salasanalla "secret".

## Uuden käyttäjän luominen
Kirjautumisnäkymässä on mahdollista luoda uusi käyttäjä painamalla "create user"-painiketta. Uusi käyttäjä luodaan syöttämällä valitsemasi käyttäjänimi ja salasana toistetusti niitä vastaaviin kenttiin ja painamalla "create user"-painiketta. Käyttäjän luomisen jälkeen sovellus siirtyy takaisin kirjautumisnäkymään

## Projektin valinta
Kirjauduttua on käyttäjän valittava projekti. Tämä onnistuu valitsemalla projekti listasta, jossa on lueteltu kaikki projektit, joihin kyseisellä käyttäjällä on lupa osallistua. Projektin valinta vahvistetaan painamalla 

