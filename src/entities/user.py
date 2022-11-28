class User:
    def __init__(self, db_id, username) -> None:
        self.db_id = db_id
        self.username = username
        self.current_project = None
        self.projects = []
