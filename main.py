from fastapi import FastAPI
from routes.user import user_router
from routes.event import event_router
from routes.registration import registration_router
 
app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(event_router, prefix = "/events", tags=["Events"])
app.include_router(registration_router, prefix = "/registations", tags=["Registrations"])
