from sqlalchemy import Column, String, Integer
from sqlalchemy import relationship
from database import Base

class Student(Base):
    __tablename__='students'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    perfil = relationship("Profile",
     back_populates="student",
     uselist=False,
     cascade="all, delete-orphan")


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    adress = Column(String)
    student_id = Column(Integer,
    ForeignKey('students.id'),
    unique=True
    )
    student = relationship(
        'student',
        back_populates='profile'
        
    )