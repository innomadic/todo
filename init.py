from models import Base, engine 

def initialize_db():
    Base.metadata.create_all(engine)