from fastapi import APIRouter
from schemas.user import UserCreate, UserUpdate
from models.user import User as UserModel
from CRUD.user import user_crud

user_router = APIRouter()

#get users endpoint
@user_router.get("", status_code = 200)
def get_all_users():
    return user_crud.get_list_of_users()

#Creat users endpoint
@user_router.post("", status_code = 201)
def  creat_user(user_data : UserCreate):
    return user_crud.add_user(user_data)

#Get an user by id
@user_router.get("/{id}", status_code = 200)
def get_user_by_id(user_id : int):
    return user_crud.get_user_with_id(user_id)

#Update users details
@user_router.put("/{id}", status_code= 200)
def update_user_information(user_id : int, User_update : UserUpdate):
    return user_crud.update_user(user_id, User_update)

#Delete users
@user_router.delete("", status_code = 200)
def delete_users(user_id : int):
    return user_crud.delete_users(user_id)