from app.Connections import sqlite_connection
from app.Models.Entry import Entry
from app.Models.SearchQuery import SearchQuery
from app.Handlers import faq_handler as faqH
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

router = APIRouter()
#Ruta para crear una Q&A
@router.post("/api/faq")
def add_faqC(entry: Entry,session: Session = Depends(sqlite_connection.get_session)):
    return faqH.create_faq(entry,session)

#Ruta para buscar una pregunta similar.
@router.post("/api/search")
def search_faqC(req: SearchQuery, session: Session = Depends(sqlite_connection.get_session)):
    try:
        entries = session.exec(select(Entry)).all()
        return faqH.search_faq(req,entries)
    except Exception as e:
        return {"status": "error", "detail": str(e)}

#Ruta para restaurar base de datos con la semilla.
@router.post("/api/faq/reset")
def reset_faqC(session: Session = Depends(sqlite_connection.get_session)):
    return faqH.reset_faq(session)

#Ruta para obtener todas las preguntas (testing)
@router.get("/api/faq/all")
def get_all_faqC(session: Session = Depends(sqlite_connection.get_session)):
    return faqH.get_all(session)

@router.get("/api/faq/{id}")
def get_one(id:int,session: Session = Depends(sqlite_connection.get_session)):
    try:
        entry = session.exec(select(Entry).where(Entry.id == id)).first()
        return entry
    except Exception as e:
        return {"status": "error", "detail": str(e)}