from typing import Optional
from pydantic import BaseModel

class EventBase(BaseModel):
    title : str
    location : str
    date : str
    is_open : bool = True
    
class EventCreate(EventBase):
    is_open : bool = True

class Event(EventCreate):
    id : int
    
class EventUpdate(BaseModel):
    title : Optional[str] = None
    location : Optional[str] = None
    date : Optional[str] = None
    is_open : bool = True
