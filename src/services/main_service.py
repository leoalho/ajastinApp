import webbrowser
from repositories.project_repository import project_repository
from repositories.user_repository import user_repository
from entities.timer import Timer
from entities.user import User
from entities.project import Project
from utils import helpers
from utils import export

class MainService():
    """Luokka sovelluken päätoiminnallisuutta varten

    Attributes:
        user = Sovellusta käyttävä käyttäjä
        timer = Sovelluksen ajastin
    """

    def __init__(self) -> None:
        """Luokan konstruktori
        """

        self._user = None
        self._timer = Timer()

    def login(self, username, password):
        """Toiminnallisuus käyttäjätunnuksen ja salasanan validoinnille.

        Args:
            username (string): käyttäjätunnus
            password (string): salasana

        Returns:
            True, jos käyttäjätunnus on olemassa ja salasana vastaa käyttäjätunnuksen salasanaa
        """
        user = user_repository.get_user(username)
        if user and helpers.validate_password(password, user):
            self._user = User(user[0], user[1])
            self.set_projects()
            return True
        return False

    def logout(self):
        """Toiminnallisuus käyttäjän uloskirjautumiseksi
        """
        self.close_project()
        self._user = None

    def set_projects(self):
        """Hakee tietokannasta sisäänkirjautuneen käyttäjän projektit
        ja asettaa nämä User-olion projekteiksi
        """

        projects = project_repository.user_projects(self._user.db_id)
        self._user.projects = []
        for project in projects:
            self._user.projects.append(Project(project[0], project[1]))

    def get_projects(self):
        """Palauttaa kirjautuneen käyttäjän projektit

        Returns:
            []: Käyttäjän hallinnoimat projektit
        """
        return self._user.projects

    def get_project_names(self):
        """Haksee listan käyttäjän projektien nimistä

        Returns:
            []: lista kaikkien käyttäjän projekteista
        """
        projects = self.get_projects()
        names = map(lambda x: x.name, projects)
        return list(names)

    def get_current_project(self):
        """Palauttaa käsiteltävissä olevan projektin
        """
        return self._user.current_project

    def set_current_project(self, project_name):
        """Asettaa projektin nykyiseksi projektiksi

        Args:
            project_name (string): projektin nimi
        """
        for project in self._user.projects:
            if project.name == project_name:
                self._user.current_project = project

    def get_username(self):
        """Palauttaa kirjautuneen käyttäjän käyttäjätunnuksen
        """
        if self._user:
            return self._user.username
        return None

    def tick(self):
        """Lisää nykyiseen ajastimeen yhden sekunnin lisää

        Returns:
           string: tämänhetkinen aika
        """

        return self._timer.tick()

    def close_project(self):
        """Sulkee nykyisen projektin
        """

        self._timer.reset()
        self._timer.session_time = 0
        self._user.current_project = None

    def reset(self):
        """Resetoi ajastimen
        """
        startstop = self._timer.get_start_stop()
        new_time = self._timer.reset()
        project_repository.new_time(
            self._user.current_project.db_id,
            self._user.db_id, new_time, startstop[0], startstop[1])

    def toggle_timer(self):
        """Kytkee ajastimen päälle/pois
        """
        self._timer.toggle_timer()
        if not self._timer.timer_on:
            self.reset()

    def get_timer(self):
        """Palauttaa ajastimen tilan"""
        return self._timer.timer_on

    def get_current_time(self):
        """Palauttaa tämänhetkisen ajastimen ajan"""
        return self._timer.current_time

    def get_session_time(self):
        """ Palauttaa kyseisen session ajan"""
        return helpers.time_to_string(self._timer.session_time)

    def get_project_time(self):
        """Palauttaa koko projektiin käytetyn ajan"""
        project_time = project_repository.project_sum_time(self._user.current_project.db_id)
        return helpers.time_to_string(project_time[0])

    def get_time_per_day(self):
        """Palauttaa ajat viimeisten päivien ajalta

        Returns:
            string: Lista ajoista viimeisten päivien ajan
        """
        times = project_repository.time_per_day(self._user.current_project.db_id)
        result = "TIme spent on project during last days:\n"
        for time in times:
            result += f"{time[0]}: {helpers.time_to_string(time[1])} \n"
        return result

    def export(self, filetype):
        """Luo tulosteen viimeisten päivien ajanotosta

        Args:
            filetype (string): tiedostomuoto, john tiedosto halutaa exportaa (txt tai pdf)

        Returns:
            palauttaa uuden tiedoston nimen
        """
        filename = export.export(
            filetype,
            self._user.username,
            self._user.current_project.name,
            project_repository.time_per_day(self._user.current_project.db_id),
            self.get_project_time())

        return filename

    def create_user(self, username, password):
        """Luo uuden käyttäjätunnuksen

        Args:
            username (string): käyttäjätunnus
            password (string): salasana
        """
        hashed_password = helpers.hash_password(password)

        user_repository.create_user(username, hashed_password)

    def create_project(self, project_name):
        """Luo uuden projektin

        Args:
            project_name (project_name): uuden projektin nimi
        """
        project_repository.create_project(self._user.db_id, project_name)
        self.set_projects()

    def open_help(self):
        """Avaa selaimessa linkin käyttöohjeeseen
        """

        webbrowser.open(
            'https://github.com/leoalho/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md')
