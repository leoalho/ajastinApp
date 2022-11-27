class User:
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
        self.current_project = None
        self.projects = []
