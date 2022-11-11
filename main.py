from fastapi import FastAPI  

app = FastAPI ()

@app.get ("/saludo")
async def root():

    return {"message": "Hola MisionTIC 2022"}

@app.get ("/usuarios/{user_id}")
async def user(user_id : int):
    return {"user_id": user_id}

courses_list = [{"nombre": "Fundamentos de Programacion"}, {"nombre": "Programacion basica"}, {"nombre": "Desarrollo de Software"}, {"nombre": "Desarrollo de Aplicaciones Web"}]

@app.get ("/cursos/")
async def read_item(skip: int=0 , limit: int=10):
    return courses_list[skip: skip+limit]