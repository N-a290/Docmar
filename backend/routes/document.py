from fastapi import APIRouter
from config.db import client
from schemas.document import documentEntity, documentsEntity
from models.document import Document

document_router = APIRouter()

@document_router.get('/document')
def find_all_document():
    return documentsEntity(client.Misiontic.Documents.find()) 

@document_router.post('/document')
def create_document(document: Document):
    new_document = dict(document)

    id = client.Misiontic.Documents.insert_one(new_document).inserted_id

    return str(id)

@document_router.get('/document/{id}')
def find_document():
    return 'helloworld'

@document_router.put('/document/{id}')
def change_document():
    return 'helloworld'

@document_router.delete('/document/{id}')
def delete_document():
    return 'helloworld'