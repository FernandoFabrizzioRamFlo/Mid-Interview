from app.Functions import NPL_Functions as nplFun
import numpy as np

import json
def create_faq(entry,session):
    entry.vector = nplFun.vectorize(entry.question)
    entry.vector = json.dumps(entry.vector.tolist(),separators=(",",":"))
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return {"vector":str(entry)}

def search_faq(req,session,entries):
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