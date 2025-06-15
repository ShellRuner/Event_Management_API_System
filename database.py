from models.user import User
from models.event import Event
from models.speaker import Speaker
from models.registration import Registration
#Users in-memeory database
Users : list[User] = []

#Events in-memory database
Events : list[Event] = []

#Speakers in-memory database
Speakers : dict[Speaker] = {
    "1" : {
        "id" : 1,
        "name" : "Tony Robbins",
        "topic" : "Personal development, peak performance, wealth mastery"
        },
    
    "2" : {
        "id" : 2,
        "name" : "Eric Thomas",
        "topic" : "Motivation, education, hustle culture"
        },
    
    "3" : {
        "id" : 3,
        "name" : "Les Brown",
        "topic" : "Overcoming adversity, goal-setting, self-belief"
    }
}

#Registration database
Registrations : dict[Registration] = {}

#Record of users registrations
RegistrationRecords = {}

#Records of events which every user has registered
# Events_By_User database logic :
    # {user_id  : [list of id of event the specific user has registered]}
Events_By_User = {}

#Records of users that had registered to a specific event
#Users_By_Event database logic:
    # {event_id : [list of id of users that had registered to that particular event]}
Users_By_Event = {}