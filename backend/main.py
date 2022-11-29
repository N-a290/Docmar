from fastapi import FastAPI
from routes.document import document_router
from routes.user import user_router

app = FastAPI ()

app.include_router(document_router)
app.include_router(user_router)

