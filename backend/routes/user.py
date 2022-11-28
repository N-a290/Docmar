from fastapi import APIRouter
from config.db import client
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/user')
def find_all_user():
    return usersEntity(client.Misiontic.User.find()) 

@user.post('/user')
def create_user(user: User):
    new_user = dict(user)

    id = client.Misiontic.User.insert_one(new_user).inserted_id

    return str(id)

@user.get('/user/{id}')
def find_user():
    return 'helloworld'

@user.put('/user/{id}')
def edit_user():
    return 'helloworld'

@user.delete('/user/{id}')
def delete_user():
    return 'helloworld'