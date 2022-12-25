# Testausdokumentti

Sovellusta on testattu automaattisten yksikkö- ja integraatiotesteillä sekä manuaalisesti järjestelmätason testeillä

## Ykikkö- & Integraatiotestaus

Yksikkötestaus tapahtuu juurihakemiston .env.test määrittelemän tietokannan tiedostojen perusteella.

Repositorioien testaus tapahtuu user_repository ja project_repository testiluokilla. Sovelluslogiikan testaus tapahtuu main_service testailuokalla.

## Testauskattavuus 

Projektin testauskattavuus on 70%. Ulkopuolelle on jäänyt erityisesti eksporttauksen ja hashauksen testaaminen ajanpuutteen vuoksi.

![](.kuvat/coverage.png)

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

Sovellus on alustettu käyttöohjetta noudattaen Windows 11:lla, että Linuxilla. Samala on testattu myös eri tietokantojen nimiä .env-muuttujien kautta

Järjestelmätetauksessa on käyty läpi kaikki määrittelydokumentin kohdat. Testauksessa on pyritty aiheuttamaan virhetilanteita ja katsomaan miten sovellus reagoi näihin.