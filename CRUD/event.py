from schemas.event import EventCreate, EventUpdate
from models.event import Event as EventModel
from database import Events

class Event_CRUD():
    @staticmethod
    #method that allow to list all events
    def list_all_events():
        return Events
    
    @staticmethod
    #method that allow to creat an event
    def creat_event(event_data : EventCreate):
        event_id = len(Events) + 1
        event = EventModel(id = event_id, **event_data.model_dump())
        Events.append(event)
        return Events
    
    @staticmethod
    #method that allow to get an event detail with its id
    def get_event_by_id(event_id : int):
        for event in Events:
            if event.id == event_id:
                return Events[event_id - 1]
        return {"message" : "This event don't exist"}
    
    @staticmethod
    def update_events(event_id : int, event_update : EventUpdate):
        for event in Events:
            if event.id == event_id:
                if event_update.title is not None:
                    event.title = event_update.title
                if event_update.location is not None:
                    event.location = event_update.location
                if event_update.date is not None:
                    event.date = event_update.date
                    
                event.is_open = event_update.is_open
                return Events[event_id - 1]
        return {"message" : "Event don't exit"}
    
    @staticmethod
    #methdo that allows to delete events
    def delete_events(user_id : int):
        for event in Events:
            if event.id == user_id:
                del Events[user_id - 1]
                return {"message" : "Event delete successfully"}
        return {"message" : "Event not found"}
        
            
event_crud = Event_CRUD()