from pydantic import BaseModel

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int
    
class CreateRegistration(RegistrationBase):
    registration_date: str
    attended: bool = True

class Registration(CreateRegistration):
    id: int
    