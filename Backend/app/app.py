#imports necesarios para ejecución del server
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
#imports necesarios para función modular.
from app.Middleware import cors
from app.Controllers import faq_controller
from app.Connections import sqlite_connection

#Carga variables de entorno para facilitar configuración
load_dotenv()
PORT = int(os.getenv("PORT"))
ORIGINS= os.getenv("ORIGINS")
HOST=os.getenv("HOST")
RESET = os.getenv("RESET")

server = FastAPI()

#Se habilita CORS middleware para conexión entre servicios.
cors.add_cors_middleware(server,ORIGINS)

#router para rutas
server.include_router(faq_controller.router)

#inicia la base de datos y valida su contenido durante el server startup
@server.on_event("startup")
async def on_startup():
    sqlite_connection.initialize_bd()
    sqlite_connection.validate_db_content()


#Facilita la ejecución desde terminal/Dockerfile
if __name__ == "__main__":
    uvicorn.run("app.app:server", host=HOST, port=PORT, reload=True)
