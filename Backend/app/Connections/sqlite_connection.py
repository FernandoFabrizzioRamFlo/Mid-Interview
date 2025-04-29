from sqlmodel import SQLModel, create_engine, Session
from app.Handlers.faq_handler import validate_data
from app.Models.Entry import Entry

#Configura conexión a sqllite
sqlite_file = "app/Connections/Entry.db"
sqlite_url = f"sqlite:///{sqlite_file}"
engine = create_engine(sqlite_url, echo=True)

def initialize_bd():
    SQLModel.metadata.create_all(engine)

#genera sesión para uso en todos los módulos (no sólo endpoints)
def get_session():
    return Session(engine)

#Valida el contenido de la base de datos al iniciar.
def validate_db_content():
    with get_session() as session:
        return validate_data(session)
    