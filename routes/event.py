from fastapi import APIRouter
from CRUD.event import event_crud
from schemas.event import EventCreate, EventUpdate

event_router = APIRouter()

#get all events in the list
@event_router.get("", status_code = 200)
def get_all_events():
    return event_crud.list_all_events()

#creat an event
@event_router.post("", status_code = 201)
def creat_event(event_data : EventCreate):
    return event_crud.creat_event(event_data)

#get an evnt by id
@event_router.get("/{id}", status_code = 200)
def get_event_by_id(id : int):
    return event_crud.get_event_by_id(id)

#update the event details
@event_router.put("/{id}", status_code = 200)
def update_events(id : int, event_update : EventUpdate):
   return event_crud.update_events(id, event_update)

#delete events
@event_router.delete("/{id}", status_code = 200)
def delete_events(id : int):
    return event_crud.delete_events(id)