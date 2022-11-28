from fastapi import FastAPI
from routes.document import document_router

app = FastAPI ()

app.include_router(document_router)