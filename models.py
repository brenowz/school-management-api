from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

# student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    enrollments = relationship(
        'Enrollment',
        back_populates='student'
    )

    # Relacionamento 1 para 1: Um aluno possui apenas um perfil (uselist=False)
    # cascade='all, delete-orphan' garante que se o aluno for deletado, o perfil também será
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


    student = relationship('Student', back_populates='profile')


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    specialty = Column(String, nullable=True)


    subjects = relationship("Subject", back_populates="teacher")


class Subject(Base):
    __tablename__ = 'subjects'

    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)

   
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

   
    teacher = relationship("Teacher", back_populates="subjects")

    enrollments = relationship("Enrollment", back_populates="subject")



class Enrollment(Base):
    __tablename__ = "enrollments"


    id = Column(Integer, primary_key=True, index=True)
    
