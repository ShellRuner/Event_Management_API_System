from database import Users
from schemas.user import UserCreate, UserUpdate
from models.user import User as UserModel
class User_CRUD:
    @staticmethod
    #get the list of all users method
    def get_list_of_users():
        return Users
    
    @staticmethod
    #create user method
    def add_user(user_data: UserCreate):
        user_id = len(Users) + 1
        user = UserModel(id = user_id, **user_data.model_dump())
        Users.append(user)
        return user
    
    @staticmethod
    #get an user by id
    def get_user_with_id(user_id : int):
        for user in Users:
            if user.id == user_id:
                return user
        return None
    
    @staticmethod
    def update_user(user_id : int, user_update : UserUpdate):
        for user in Users:
            if user.id == user_id:
                if user_update.name is not None:
                    user.name = user_update.name
                if user_update.email is not None:
                    user.email = user_update.email
                user.is_active = user_update.is_active
        return Users[user_id - 1]
    
    @staticmethod
    def delete_users(user_id : int):
        for user in Users:
            if user.id == user_id:
                del Users[user_id]
                return {"message" : "Delete successfully"}
        return {"message" : "This user don't exist"}

user_crud = User_CRUD()