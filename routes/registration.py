from fastapi import APIRouter
from schemas.registration import CreateRegistration
from services.Registration import registration_service


registration_router = APIRouter()

#register user for an event
@registration_router.post("/", status_code= 201)
def user_registration(user_registed : CreateRegistration):
    return registration_service.user_registration(user_registed)

#view registrations for a specific user
@registration_router.get("/users/{id}", status_code= 200)
def view_user_registrations(user_id : int):
    return registration_service.view_user_registrations(user_id)

#view all registrations
@registration_router.get("/", status_code=200)
def view_all_registrations():
    return registration_service.view_all_registrations()