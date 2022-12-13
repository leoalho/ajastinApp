class Project:
    """Luokka kuvaamaan yksittäistä projektia
    """
    def __init__(self, db_id, name) -> None:
        """Luokan konstruktori

        Args:
            db_id (string): tietokannan id projektille
            name (string): projektin nimi
        """
        self.db_id = db_id
        self.name = name
        self.logs = [] # No implementation
        self.owners = [] # No implementation
