from fastapi import FastAPI
from routes.document import document_router
from routes.user import user_router

app = FastAPI (
    title="DOCMAR",
    description="Servicio de Gestión documental, hecho con FastAPI y conectado con una base de datos de MongoDB Atlas",
    version="0.1"
)

app.include_router(document_router)
app.include_router(user_router)

