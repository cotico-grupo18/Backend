from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/persons/")
def create_person(person: Person):
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
        return person


@router.get("/persons/")
def get_persons():
    with Session(engine) as session:
        statement = select(Person)
        persons = session.exec(statement).all()
        return persons


@router.delete("/persons/{person_id}")
def delete_person(person_id: int):
    with Session(engine) as session:
        statement = select(Person).where(Person.id == person_id)
        person = session.exec(statement).first()
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        session.delete(person)
        session.commit()
        return {"message": "Person deleted successfully"}


@router.put("/persons/{person_id}")
def update_person(person_id: int, updated_person: Person):
    with Session(engine) as session:
        statement = select(Person).where(Person.id == person_id)
        person = session.exec(statement).first()
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        for key, value in updated_person.dict().items():
            setattr(person, key, value)
        session.add(person)
        session.commit()
        session.refresh(person)
        return person
