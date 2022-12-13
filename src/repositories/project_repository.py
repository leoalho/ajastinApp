from database_connection import get_database_connection

class ProjectRepository:
    """Luokka tietokannan projekteihin liittyvien SQL komentoja varten
    """

    def __init__(self, connection) -> None:
        """Luokan konstruktori

        Args:
            connection: Rajapinta sqlite tietokantaan
        """

        self._connection = connection

    def user_projects(self, user_id):
        """Hakee kaikki käyttäjän projektit

        Args: user_id (string): käyttäjän id
        Palauttaa listan käyttäjän projekteista
        """

        projects = self._connection.execute(
            """SELECT P.id, P.projectname FROM projects P, projectOwners PO
            WHERE P.id=PO.project_id and PO.user_id=?""", [user_id]).fetchall()
        return projects

    def project_sum_time(self, project_id):
        """Hakee aikamäärän jota projektiin on käytetty

        Args: project_id (string): haettavan projektin id

        Palauttaa kokonaislukuna projektiin käytetyn ajan
        """

        time = self._connection.execute(
            """SELECT SUM(time) FROM logs
            WHERE project_id=?""",[project_id]).fetchone()
        return time

    def create_project(self, user_id, project_name):
        """Luo uuden projektin

        Args:
            user_id (string): Käyttäjän id, joka luo uuden projektin
            project_name (string): Uuden projektin nimi
        """

        cursor=self._connection.cursor()
        cursor.execute("INSERT INTO projects(projectname) VALUES(?)", [project_name])
        project_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO projectOwners(project_id, user_id) VALUES(?,?)",
            [project_id, user_id])

    def project_all_times(self, project_id):
        """Hakee kaikki projektiin liittyvät ajanottoinstanssit

        Args:
            project_id (string): Haettavan projektin id

        Palauttaa listan ajanotoista
        """

        times = self._connection.execute(
            """SELECT * FROM logs
            WHERE project_id=?""",[project_id]).fetchall()
        return times

    def new_time(self, project_id, user_id, time, start_time, end_time):
        """Luo uuden ajanottoinstanssin

        Args:
            project_id (string): käsiteltävän projektin id
            user_id (string): Käyttäjän id
            time: ajanoton aika sekunteina
            start_time: aikaleima, kun ajanotto alkoi
            end_time: aikaleima, kun ajanotto loppui
        """
        self._connection.execute(
            """INSERT INTO logs (project_id, user_id, time, startTime, endTime)
            VALUES (?,?,?,?,?)""",[project_id, user_id, time, start_time, end_time])

    def time_per_day(self, project_id):
        """Hakee summan kuinka paljon aikaa projektiin on käytetty per päivä

        Args:
            project_id: kyseisen projektin id

        Palauttaa listan ajanotoista
        """

        times = self._connection.execute(
            """SELECT DATE(startTime) as date,SUM(time)
            FROM logs WHERE project_id=? GROUP BY date;""",[project_id]).fetchall()
        return times


project_repository = ProjectRepository(get_database_connection())
