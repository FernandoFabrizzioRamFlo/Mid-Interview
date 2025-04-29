from app.Connections import sqlite_connection
from app.Models.Entry import Entry
from app.Models.SearchQuery import SearchQuery
from app.Handlers import faq_handler as faqH
from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter()

@router.post("/api/faq/add")
def add_faq(entry: Entry,session: Session = Depends(sqlite_connection.get_session)):
    return faqH.create_faq(entry,session)

@router.post("/api/faq/search")
def search_faq(req: SearchQuery, session: Session = Depends(sqlite_connection.get_session)):
    entries = session.query(Entry).all()
    return faqH.search_faq(req,session,entries)

#@router.post("api/faq/plant-seed")
#def populate_faq(req:json):
#    return faH.create_faq(req)