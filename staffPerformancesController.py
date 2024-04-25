from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

router = APIRouter()

@router.post("/staff_performances/")
def create_staff_performance(staff_performance: StaffPerformance):
    with Session(engine) as session:
        session.add(staff_performance)
        session.commit()
        session.refresh(staff_performance)
        return staff_performance
    


@router.get("/staff_performances/")
def get_staff_performances():
    with Session(engine) as session:
        statement = select(StaffPerformance)
        staff_performances = session.exec(statement).all()
        return staff_performances
    


@router.delete("/staff_performances/{staff_performance_id}")
def delete_staff_performance(staff_performance_id: int):
    with Session(engine) as session:
        statement = select(StaffPerformance).where(StaffPerformance.id == staff_performance_id)
        staff_performance = session.exec(statement).first()
        if not staff_performance:
            raise HTTPException(status_code=404, detail="Staff Performance not found")
        session.delete(staff_performance)
        session.commit()
        return {"message": "Staff Performance deleted successfully"}
    


@router.put("/staff_performances/{staff_performance_id}")
def update_staff_performance(staff_performance_id: int, updated_staff_performance: StaffPerformance):
    with Session(engine) as session:
        statement = select(StaffPerformance).where(StaffPerformance.id == staff_performance_id)
        staff_performance = session.exec(statement).first()
        if not staff_performance:
            raise HTTPException(status_code=404, detail="Staff Performance not found")
        for key, value in updated_staff_performance.dict().items():
            setattr(staff_performance, key, value)
        session.add(staff_performance)
        session.commit()
        session.refresh(staff_performance)
        return staff_performance