from typing import List, Optional
from pydantic import BaseModel

# profile schemas
class ProfileCreate(BaseModel):
    age: int
    adress: str


class Profile(BaseModel):
    id: int
    age: int
    adress: str

    class Config:
        from_attributes = True


# student schemas
class StudentCreate(BaseModel):
    name: str
    email: str
    profile: ProfileCreate


class Student(BaseModel):
    id: int
    name: str
    profile: Optional[Profile] = None

    class Config:
        from_attributes = True


# teacher schemas
class TeacherCreate(BaseModel):
    name: str
    email: str
    specialty: Optional[str] = None


class Teacher(BaseModel):
    id: int
    name: str
    email: str
    specialty: Optional[str] = None

    class Config:
        from_attributes = True


# subject schemas
class SubjectCreate(BaseModel):
    name: str
    code: str
    teacher_id: Optional[int] = None


class Subject(BaseModel):
    id: int
    name: str
    code: str
    teacher_id: Optional[int] = None

    class Config:
        from_attributes = True


# enrollment schemas
class EnrollmentCreate(BaseModel):
    student_id: int
    subject_id: int


class Enrollment(BaseModel):
    id: int
    student_id: int
    subject_id: int
    grade: Optional[float] = None

    class Config:
        from_attributes = True