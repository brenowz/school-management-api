from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    profile = relationship(
        'Profile',
        back_populates='student',
        uselist=False,
        cascade='all, delete-orphan',
    )


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    adress = Column(String)
    student_id = Column(
        Integer, ForeignKey('students.id'), unique=True
    )

    # Fix: 'Student' com S maiúsculo
    student = relationship('Student', back_populates='profile')