from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

router = APIRouter()



@router.post("/reservations/")
def create_reservation(reservation: Reservation):
    with Session(engine) as session:
        session.add(reservation)
        session.commit()
        session.refresh(reservation)
        return reservation
    

@router.get("/reservations/")
def get_reservations():
    with Session(engine) as session:
        statement = select(Reservation)
        reservations = session.exec(statement).all()
        return reservations
    

@router.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    with Session(engine) as session:
        statement = select(Reservation).where(Reservation.id == reservation_id)
        reservation = session.exec(statement).first()
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        session.delete(reservation)
        session.commit()
        return {"message": "Reservation deleted successfully"}
    

@router.put("/reservations/{reservation_id}")
def update_reservation(reservation_id: int, updated_reservation: Reservation):
    with Session(engine) as session:
        statement = select(Reservation).where(Reservation.id == reservation_id)
        reservation = session.exec(statement).first()
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        for key, value in updated_reservation.dict().items():
            setattr(reservation, key, value)
        session.add(reservation)
        session.commit()
        session.refresh(reservation)
        return reservation