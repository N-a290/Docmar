from fastapi import APIRouter, Response, status
from config.db import client
from schemas.document import documentEntity, documentsEntity
from models.document import Document
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

document_router = APIRouter()

@document_router.get('/api/document', response_model=list[Document], tags=["Documentos"])
def find_all_document():
    return documentsEntity(client.Misiontic.Documents.find()) 

@document_router.post('/api/document', response_model=Document, tags=["Documentos"])
def create_document(document: Document):
    id = client.Misiontic.document.insert_one(document).inserted_id
    selected_document = client.Misiontic.Documents.find_one({"_id": id})

    return documentEntity(selected_document)

@document_router.get('/api/document/{id}', response_model=Document, tags=["Documentos"])
def find_document(id: str):
    return documentEntity(client.Misiontic.Documents.find_one({"_id": ObjectId(id)}))

@document_router.put('/api/document/{id}', response_model=Document, tags=["Documentos"])
def update_document(id: str, document: Document):
    client.Misiontic.document.find_one_and_update({"_id": ObjectId(id)}, {'$set': dict(document)})
    updated_document = client.Misiontic.Documents.find_one({"_id": ObjectId(id)})
    
    return documentEntity(updated_document)

@document_router.delete('/api/document/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Documentos"])
def delete_document(id: str):
    documentEntity(client.Misiontic.Documents.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)