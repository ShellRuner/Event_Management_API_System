from pydantic import BaseModel
from typing import Optional

#User pydantic schema
class UserBase(BaseModel):
    name : str
    email : str
    
class UserCreate(UserBase):
    is_active : bool = True

    
class UserUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    is_active : bool = True

class User(UserCreate):
    id : int