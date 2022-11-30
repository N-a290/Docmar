from fastapi import APIRouter, Response, status
from config.db import client
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user_router = APIRouter()

@user_router.get('/api/user', response_model=list[User], tags=["Usuarios"])
def find_all_user():
    return usersEntity(client.Misiontic.User.find()) 

@user_router.post('/api/user', response_model=User, tags=["Usuarios"])
def create_user(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])

    id = client.Misiontic.User.insert_one(new_user).inserted_id
    selected_user = client.Misiontic.User.find_one({"_id": id})

    return userEntity(selected_user)

@user_router.get('/api/user/{id}', response_model=User, tags=["Usuarios"])
def find_user(id: str):
    return userEntity(client.Misiontic.User.find_one({"_id": ObjectId(id)}))

@user_router.put('/api/user/{id}', response_model=User, tags=["Usuarios"])
def update_user(id: str, user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    
    client.Misiontic.User.find_one_and_update({"_id": ObjectId(id)}, {'$set': dict(new_user)})
    updated_user = client.Misiontic.User.find_one({"_id": ObjectId(id)})
    
    return userEntity(updated_user)

@user_router.delete('/api/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def delete_user(id: str):
    userEntity(client.Misiontic.User.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)