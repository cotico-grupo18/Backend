from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

router = APIRouter()

@router.post("/residence_places/")
def create_residence_place(residence_place: ResidencePlace):
    with Session(engine) as session:
        session.add(residence_place)
        session.commit()
        session.refresh(residence_place)
        return residence_place
    
@router.get("/residence_places/")
def get_residence_places():
    with Session(engine) as session:
        statement = select(ResidencePlace)
        residence_places = session.exec(statement).all()
        return residence_places
    


@router.delete("/residence_places/{residence_place_id}")
def delete_residence_place(residence_place_id: int):
    with Session(engine) as session:
        statement = select(ResidencePlace).where(ResidencePlace.id == residence_place_id)
        residence_place = session.exec(statement).first()
        if not residence_place:
            raise HTTPException(status_code=404, detail="Residence Place not found")
        session.delete(residence_place)
        session.commit()
        return {"message": "Residence Place deleted successfully"}
    

@router.put("/residence_places/{residence_place_id}")
def update_residence_place(residence_place_id: int, updated_residence_place: ResidencePlace):
    with Session(engine) as session:
        statement = select(ResidencePlace).where(ResidencePlace.id == residence_place_id)
        residence_place = session.exec(statement).first()
        if not residence_place:
            raise HTTPException(status_code=404, detail="Residence Place not found")
        for key, value in updated_residence_place.dict().items():
            setattr(residence_place, key, value)
        session.add(residence_place)
        session.commit()
        session.refresh(residence_place)
        return residence_place