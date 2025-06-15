class Registration:
    def __init__(self, id : int, user_id : int, event_id : int, registration_date : str, attended : bool):
        self.id = id
        self.user_id = user_id
        self.event_id = event_id
        self.registration_date = registration_date
        self.attented = attended