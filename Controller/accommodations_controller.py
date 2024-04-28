from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/accommodations/")
def create_accommodation(accommodation: Accommodation):
    with Session(engine) as session:
        session.add(accommodation)
        session.commit()
        session.refresh(accommodation)
        return accommodation


@router.get("/accommodations/")
def get_accommodations():
    with Session(engine) as session:
        statement = select(Accommodation)
        accommodations = session.exec(statement).all()
        return accommodations


@router.delete("/accommodations/{accommodation_name}")
def delete_accommodation(accommodation_name: str):
    with Session(engine) as session:
        statement = select(Accommodation).where(
            Accommodation.name == accommodation_name
        )
        accommodation = session.exec(statement).first()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        session.delete(accommodation)
        session.commit()
        return {"message": "Accommodation deleted successfully"}


@router.put("/accommodations/{accommodation_name}")
def update_accommodation(accommodation_name: str, updated_accommodation: Accommodation):
    with Session(engine) as session:
        statement = select(Accommodation).where(
            Accommodation.name == accommodation_name
        )
        accommodation = session.exec(statement).first()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        for key, value in updated_accommodation.dict().items():
            setattr(accommodation, key, value)
        session.add(accommodation)
        session.commit()
        session.refresh(accommodation)
        return accommodation
