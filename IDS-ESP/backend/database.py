from models import SQLModel, create_engine, Session

DATABASE_UDL = "postgresql://audituser:securepass@localhost/rogue_audit"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    return Session(engine)
