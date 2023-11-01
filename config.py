from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    conn = 'sqlite:///projeto.db'
    engine=create_engine(conn, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
