from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload

from database import SessionLocal, engine
import models, schemas


models.Base.metadata.create_all(bind=engine)


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


@app.get('/students/', response_model=List[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    students = (
        db.query(models.Student)
        .options(joinedload(models.Student.profile))
        .all()
    )
    return students


@app.post('/teachers/', response_model=schemas.Teacher)
def create_teacher(
    teacher: schemas.TeacherCreate, db: Session = Depends(get_db)
):
    
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher



@app.get('/teachers/', response_model=List[schemas.Teacher])
def list_teachers(db: Session = Depends(get_db)):
    teachers = db.query(models.Teacher).all()
    return teachers



@app.post('/subjects/', response_model=schemas.Subject)
def create_subject(
    subject: schemas.SubjectCreate, db: Session = Depends(get_db)
):
    db_subject = models.Subject(**subject.model_dump())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject


@app.get('/subjects/', response_model=List[schemas.Subject])
def list_subjects(db: Session = Depends(get_db)):
    subjects = db.query(models.Subject).all()
    return subjects


@app.post('/enrollments/', response_model=schemas.Enrollment)
def create_enrollment(
    enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)
):
    db_enrollment = models.Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment



@app.get('/enrollments/', response_model=List[schemas.Enrollment])
def list_enrollments(db: Session = Depends(get_db)):
    enrollments = db.query(models.Enrollment).all()
    return enrollments