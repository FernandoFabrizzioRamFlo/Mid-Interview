from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from app.Middleware import cors
from app.Controllers import faq_controller
from app.Connections import sqlite_connection

#Carga variables de entorno para mejores prácticas.
load_dotenv()
PORT = int(os.getenv("PORT"))
ORIGINS= os.getenv("ORIGINS")
HOST=os.getenv("HOST")


server = FastAPI()

#Se habilita CORS.
cors.add_cors_middleware(server,ORIGINS)

#router para rutas faq
server.include_router(faq_controller.router)

@server.on_event("startup")
async def on_startup():
    sqlite_connection.initialize_bd()

#Permite ejecutar desde consola con "py app.py"
if __name__ == "__main__":
    
    uvicorn.run("app.app:server", host=HOST, port=PORT, reload=True)
