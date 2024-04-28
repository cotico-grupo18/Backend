from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/staff/")
def create_staff(staff: Staff):
    with Session(engine) as session:
        session.add(staff)
        session.commit()
        session.refresh(staff)
        return staff


@router.get("/staff/")
def get_staff():
    with Session(engine) as session:
        statement = select(Staff)
        staff = session.exec(statement).all()
        return staff


@router.delete("/staff/{staff_id}")
def delete_staff(staff_id: int):
    with Session(engine) as session:
        statement = select(Staff).where(Staff.id == staff_id)
        staff = session.exec(statement).first()
        if not staff:
            raise HTTPException(status_code=404, detail="Staff not found")
        session.delete(staff)
        session.commit()
        return {"message": "Staff deleted successfully"}


@router.put("/staff/{staff_id}")
def update_staff(staff_id: int, updated_staff: Staff):
    with Session(engine) as session:
        statement = select(Staff).where(Staff.id == staff_id)
        staff = session.exec(statement).first()
        if not staff:
            raise HTTPException(status_code=404, detail="Staff not found")
        for key, value in updated_staff.dict().items():
            setattr(staff, key, value)
        session.add(staff)
        session.commit()
        session.refresh(staff)
        return staff
