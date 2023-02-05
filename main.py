from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Text, Optional 
from pydantic import BaseModel
from typing import List


#  Se crea la instancia de FastAPI
app = FastAPI(
    title="Proyecto cafe 9 | Login microservice ",
    description="Api for login microservice",
    version="0.0.0",
)


#  A continuación se configura que todas las IPs puedan acceder a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Usuarios = [
    { 
        "id": 1,
        "usuario": "admin1",
        "permiso": "admin",
        "contraseña": "admin123"
    },
    {
        "id": 2,
        "usuario": "admin2",
        "permiso": "admin",
        "contraseña": "admin123"
    },
    {
        "id": 3,
        "usuario": "admin3",
        "permiso": "admin",
        "contraseña": "admin123"
    },
    {
        "id": 4,
        "usuario": "admin4",
        "permiso": "admin",
        "contraseña": "admin123"
    }
] 


##Elemento de la base
class Usuario(BaseModel):
     id: int
     usuario: str
     permiso: str 
     contraseña: str


##Usuario sin mostrar la contraseña
class Usuario_return(BaseModel):
     id: int
     usuario: str
     permiso: str 


#Agregando un usuario a Usuarios  
@app.post(
    path="/",
    response_model=Usuario_return, 
    summary="Agrega un usuario",
    description="Agrega un usuario a la base de datos",
    tags=["Usuarios"]
    )
async def Login_Add(
    usuario:Usuario = Body(..., example={
        "id": 1,
        "usuario": "admin1",
        "permiso": "admin",
        "contraseña": "admin123"
        }),
    ):
     Usuarios.append(usuario.dict())
     return usuario


#Enlistando todos los usuarios  
@app.get(
    path="/",
    response_model=List[Usuario_return], 
    summary="Lista de usuarios",
    description="Regresamos todos los usuarios en una lista",
    tags=["Usuarios"]
    )
async def Login_get():
     return Usuarios


#Regresando un usuario específico según su id  
@app.get(
    path="/{usuario_id}", 
    response_model=Usuario_return, 
    summary="Usuario",
    description="Regresamos un usuario específico según su id",
    tags=["Usuarios"]
    )
async def Login_get_id(usuario_id: int):
        for usuario in Usuarios:
            if usuario["id"] == usuario_id:
                return usuario
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


#Eliminando un usuario específico según su id
@app.delete(
    path="/{usuario_id}", 
    response_model=Usuario_return, 
    summary="Eliminando usuario",
    description="Eliminamos un usuario específico según su id",
    tags=["Usuarios"]
    )
async def Login_del(usuario_id: int):
        for usuario in Usuarios:
            if usuario["id"] == usuario_id:
                Usuarios.remove(usuario)
                return usuario
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


#Actualizando un usuario específico según su id    
@app.put(
    path="/{usuario_id}", 
    response_model=Usuario_return, 
    summary="Actualizar usuario",
    description="Actualizamos un usuario específico según su id",
    tags=["Usuarios"]
    )
async def Login_put(
    usuario_id: int, new_usuario: Usuario):
        for usuario in Usuarios:
            if usuario["id"] == usuario_id:
                usuario["usuario"] = new_usuario.usuario
                usuario["contraseña"] = new_usuario.contraseña
                usuario["permiso"] = new_usuario.permiso
                return usuario
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


#  Entry point
if __name__ == "__main__":
    import uvicorn
    import os
    
    start = "main:app"
    uvicorn.run(
        start, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", default=8080)), 
        reload=True
    )