# Arkkitehtuurikuvaus

## Rakenne

Luokkakaavio:

```mermaid
classDiagram
    main_service "1" -- "1" timer
    main_service "1" -- "1" user
    user "1" -- "*" project
    main_service ..> project
    main_service -- project_repository
    main_service -- user_repository
```
Pakkausrakenne:

![pakkauskaavio](./kuvat/packing_diagram.png)

## Päätoiminnallisuudet

### Käyttäjän sisäänkirjautuminen

```mermaid
sequenceDiagram
actor user
participant UI
participant MainService
participant UserRepository
participant ProjectRepository
participant helpers
user ->> UI: click "Login" button
UI ->> MainService: login("Test", "secret")
MainService ->> UserRepository: get_User("Test")
UserRepository -->> MainService: user
MainService ->> helpers: validate_password("secret", user)
helpers -->> MainService: True
MainService ->> MainService: set_projects()
MainService ->> ProjectRepository: user_projects(1)
ProjectRepository -->> MainService: projects
MainService -->> UI: True
UI ->> UI: Mover(project_view)
```
Käyttäjä painaa login-painiketta syötettetyään olemassa olevan käyttäjänimen ja oikean salasanan. Login painikkeen tapahtumankäsittelijä kutsuu Mainservicen metodia login parametreina käyttäjätunnus ja salasana. Mainservice kutsuu UserRepository olion metodia get_user parametrina käyttäjätunnus, joka tarkastaa onko tietokannassa olemassa kyseinen käyttäjätunnus ja palauttaa käyttäjätiedot. Tämän jälkeen Mainservice tarkistaa validate_password funktiolla, vastaako käyttäjän antama salasana tietokantaan tallennettua hashattua salasanaa. Seuraavaksi MainSErvice kutstuu ProjectRepositoryn metodia set_projects(), joka palauttaa sisäänkirjautuneen käyttäjän projektit. Mainservice palauttaa UI:lle True, jonka jälkeen UI muuttaa näkymäkseen project_view mover-metodin avulla.
