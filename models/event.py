#Event data  model
class Event:
    def __init__(self, id : int, title : str, location : str, date : str, is_open : str):
        self.id = id
        self.title = title
        self.location = location
        self.date = date
        self.is_open = is_open