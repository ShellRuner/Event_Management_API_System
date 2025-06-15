#User data model
class User:
    def __init__(self, id : int, name : str, email: str, is_active : bool):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active