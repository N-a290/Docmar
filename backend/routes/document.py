from fastapi import APIRouter, Response, status
from config.db import client
from schemas.document import documentEntity, documentsEntity
from models.document import Document
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

document_router = APIRouter()

# Obtener todos los elementos 
@document_router.get('/api/document', response_model=list[Document], tags=["Documentos"])
def find_all_document():
    return documentsEntity(client.Misiontic.Documents.find()) 

# Ingresar un nuevo documento 
@document_router.post('/api/document', response_model=Document, tags=["Documentos"])
def create_document(document: Document):
    new_document = dict(document)

    id = client.Misiontic.Documents.insert_one(documentEntity(new_document)).inserted_id
    selected_document = client.Misiontic.Documents.find_one({"_id": id})

    return documentEntity(selected_document)

# Obtener un documento por el id
@document_router.get('/api/document/{id}', response_model=Document, tags=["Documentos"])
def find_document(id: str):
    return documentEntity(client.Misiontic.Documents.find_one({"_id": ObjectId(id)}))

# Obtener todos los documentos que encajen en la categoría
@document_router.get('/api/document/category/{category}', response_model=list[Document], tags=["Documentos"])
def find_document(category: str):
    return documentsEntity(client.Misiontic.Documents.find({"category": {"$eq": category}}))

# Obtener todos los documentos que encajen con el tipo (Electrónico o Físico)
@document_router.get('/api/document/type/{type}', response_model=list[Document], tags=["Documentos"])
def find_document(type: str):
    return documentsEntity(client.Misiontic.Documents.find({"type": {"$eq": type}}))

# Editar o cambiar un documento
@document_router.put('/api/document/{id}', response_model=Document, tags=["Documentos"])
def update_document(id: str, document: Document):
    client.Misiontic.Documents.find_one_and_update({"_id": ObjectId(id)}, {'$set': dict(document)})
    updated_document = client.Misiontic.Documents.find_one({"_id": ObjectId(id)})
    
    return documentEntity(updated_document)

# Borrar un documento
@document_router.delete('/api/document/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Documentos"])
def delete_document(id: str):
    documentEntity(client.Misiontic.Documents.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)