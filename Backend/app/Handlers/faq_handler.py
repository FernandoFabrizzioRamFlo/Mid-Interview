from app.Functions import NPL_Functions as nplFun
from sqlmodel import select, delete
from app.Models.Entry import Entry
from pathlib import Path
import numpy as np

import json

#crea una nueva pregunta y respuesta.
def create_faq(entry,session):
    try:
        datatoVector =f'{entry.question} {entry.answer}'
        entry.vector = nplFun.vectorize(datatoVector)
        entry.vector = json.dumps(entry.vector.tolist(),separators=(",",":"))
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return {"vector":str(entry)}
    except Exception as e:
        session.rollback()
        return {"status": "error", "detail": str(e)}


#Busca la pregunta y respuesta más parecida a query del usuario.
def search_faq(req,entries):
    try:
        best=[None,-2]
        qVec = nplFun.vectorize(req.question)
        print("hello")
        for entry in entries:
            thisEntryVector = np.array(json.loads(entry.vector))
            similarity = nplFun.get_cos_similarity(qVec,thisEntryVector)
            if similarity >= best[1]:
                best[0]= entry
                best[1]= similarity
                
        return best[0]
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    
#restaura la base de datos con la semilla.
def reset_faq(session):
    try:
        print("holaaaaa")
        seed_path = Path(__file__).parent.parent /"Connections"/ "seed.json"
        print(seed_path)
        session.exec(delete(Entry))
        #lee semilla
        with open(seed_path, "r", encoding="utf-8") as f:
            entries = json.load(f)
            for entry in entries:
                entry = Entry(**entry)
                datatoVector =f'{entry.question} {entry.answer}'
                entry.vector = nplFun.vectorize(datatoVector)
                entry.vector = json.dumps(entry.vector.tolist(),separators=(",",":"))
                session.add(entry)
        session.commit()
        return 200
    except Exception as e:
        session.rollback()
        return {"status": "error", "detail": str(e)}

#valida si es necesario restaurar la base de datos con la semilla
def validate_data(session):
    try:    
        entries = session.exec(select(Entry)).all()
        if len(entries) < 50:
            return reset_faq(session)
        else:
            return {"step:": "BD validation Handler", "status": "No changes required"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

#Obtiene todos los registros.
def get_all(session):
    try:
        return session.exec(select(Entry)).all()
    except Exception as e:
        return {"status": "error", "detail": str(e)}