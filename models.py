from sqlalchemy import create_engine
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///todos.db', echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Todo(Base):
    __tablename__ = 'todo'
    text = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'<Todo id={self.id} text={self.text}>'


