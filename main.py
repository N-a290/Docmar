from fastapi import FastAPI  

app = FastAPI ()

@app.get ("/Bienvenida")
async def root():
    return {"message": "Bienvenido a DOCMAR el mayor gestor de documentos. ¡Confianza & Seguridad!"}

@app.get ("/usuarios/{user_id}")
async def user(user_id : int):
    return {"user_id": user_id}

services = [{"servicio": "Libros electrónicos"},{"servicio": "revistas"},{"servicio":"iconografias"},{"servicio":"monografias"},{"servicio":"ensayos"},{"servicio":"investigaciones"}]

@app.get ("/servicios")
async def showServices():
    return services
