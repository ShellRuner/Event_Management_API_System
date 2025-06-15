from database import Users, Events, Registrations, RegistrationRecords, Events_By_User, Users_By_Event
from schemas.registration import CreateRegistration
from models.registration import Registration as RegistrationModel


class RegistrationService:
    @staticmethod
    #method that allow to register user for an event
    def user_registration(user_registed : CreateRegistration):
        # event_id_list = []
        # user_id_list = []
        
        # registration_id = len(Registrations) + 1
        for user in Users:
            #Only active users can register
            if user.id == user_registed.user_id and user.is_active == True:
                for event in Events:
                    #Event must be open
                    if event.id == user_registed.event_id and event.is_open == True:
                        #Users cannot register more than once for the same event
                        #initialize the Event_By_User dictionary if the user id  don't exist yet
                        if user.id not in Events_By_User:
                            Events_By_User[user.id] = []
                        
                        #check if user already register to the event    
                        if event.id in Events_By_User[user.id]:
                            return {"message" : "Can't register more than once for the same event"}
                        
                        #record of events that the user has registered
                        Events_By_User[user.id].append(event.id)
                        
                        #initialize the Users_By_Event dictionary if the event id not registered yet
                        if event.id not in Users_By_Event:
                            Users_By_Event[event.id] = []
                        #record of users that had registered to a specific event
                        Users_By_Event[event.id].append(user.id)
                            
                        registration_id = len(Registrations) + 1
                        registation = RegistrationModel(registration_id,
                                                        **user_registed.model_dump())
                        Registrations[registration_id] = registation
                        
                        
                        return Registrations[registration_id]
        return {"message" : "Cannot register to this event"}
    
    @staticmethod
    def view_user_registrations(user_id : int):
        #method that allows to view registrations for a specific user
        events_registered = []
        if user_id in Events_By_User:
            for event_id in Events_By_User[user_id]:
                events_registered.append(Events[event_id - 1])
            return events_registered
        return {"message" : "this user don't register to any event"}
    
    @staticmethod
    def view_all_registrations():
        return Registrations

registration_service = RegistrationService()
                        