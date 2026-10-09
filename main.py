from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload

from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

# Fix 1: Adicionados os parênteses ()
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/students/', response_model=schemas.Student)
def create_student(
    student: schemas.StudentCreate, db: Session = Depends(get_db)
):
    db_student = models.Student(
        name=student.name, profile=models.Profile(**student.profile.dict())
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Fix 2: 'schemas.Student' (singular), 'models.Student.profile' (minúsculo) e 'return students' (variável)
@app.get('/students/', response_model=List[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    students = (
        db.query(models.Student)
        .options(joinedload(models.Student.profile))
        .all()
    )
    return students