class User:
    """Luokka kuvaamaan käyttäjää
    """
    def __init__(self, db_id, username) -> None:
        """Luokan konstruktori

        Args:
            db_id (string): Käyttäjän id tietokannassa
            username (string): Käyttäjätunnus
        """
        self.db_id = db_id
        self.username = username
        self.current_project = None
        self.projects = []
