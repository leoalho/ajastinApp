from database_connection import get_database_connection

class UserRepository:
    """Luokka käyttäjiin liittyviin tietokantametodeja varten
    """
    def __init__(self, connection) -> None:
        """Luokan konstruktori

        Args:
            connection: Rajapinta sqlite tietokantaan
        """

        self._connection = connection

    def create_user(self, username, password):
        """Luo uuden käyttäjän

        Args:
            username (string): käyttäjätunnus
            password (string): hashattu salasana
        """

        self._connection.execute(
            """INSERT INTO users (username, password) values (?,?)""",[username,password]
        )

    def all_users(self):
        """Hakee kaikki käyttäjät

        Palauttaa listan kaikista käyttäjistä_
        """
        users = self._connection.execute("SELECT * FROM users").fetchall()
        return users

    def get_user(self, username):
        """Hakee yksittäisen käyttäjän

        Args:
            username (string): käyttäjärunnus

        Palauttaa haetun käyttäjän
        """
        user = self._connection.execute(
            "SELECT * FROM users WHERE username=?",[username]).fetchone()
        return user

user_repository = UserRepository(get_database_connection())
