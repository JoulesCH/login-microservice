from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Text, Optional 
from pydantic import BaseModel

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

Usuarios = []

#  Routes
@app.get("/")
async def root():
    return {"message": "ola"}

##Elemento de la base
class Usuario(BaseModel):
     ID: int
     Permiso: str
     Contraseña: int

#Agregando un usuario a Usuarios  
@app.post("/Add")
async def Login_Add(usuario:Usuarios, contraseña:Usuarios, permiso:Usuarios):
     Usuarios.append(usuario)
     Usuarios.append(contraseña)
     Usuarios.append(permiso)
     return{"Usuario":Usuarios}


app.get('/Usuarios/{Usuarios_id}')
def get_post():
    return "received"

#Modificar usuarios
@app.put("/Modify")
async def Login_Mod(usuarop: Usuario, contraseña: Usuario, permiso: Usuario):
     for index, Usuario in enumerate(Usuarios):
         if(Usuario["Usuarios_ID"]==Usuario and contraseña["Usuarios_ID"]==contraseña):
             Usuarios[index].update(Usuario)
             return{"Usuario":Usuarios}

#Borrar usuarios
@app.delete("/Delete")
async def Login_Del(usuario:Usuarios, contraseña:Usuarios, permiso:Usuarios):
     for index, usuario in enumerate(Usuarios):
         if(usuario["Usuario_ID"]==usuario and contraseña["Usuarios_ID"]==contraseña):
             del Usuarios[index]
             return{"Usuario":Usuarios}


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