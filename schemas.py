from typing import List, Optional
from pydantic import BaseModel


# 1. Definimos os Schemas de Profile primeiro:
class ProfileCreate(BaseModel):
    age: int
    adress: str


class Profile(BaseModel):
    id: int
    age: int
    adress: str

    class Config:
        from_attributes = True


# 2. Agora podemos usar Profile dentro dos Schemas de Student:
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