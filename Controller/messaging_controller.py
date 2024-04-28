from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/messagings/")
def create_messaging(messaging: Messaging):
    with Session(engine) as session:
        session.add(messaging)
        session.commit()
        session.refresh(messaging)
        return messaging
    

@router.get("/messagings/")
def get_messagings():
    with Session(engine) as session:
        statement = select(Messaging)
        messagings = session.exec(statement).all()
        return messagings
    

@router.delete("/messagings/{messaging_id}")
def delete_messaging(messaging_id: int):
    with Session(engine) as session:
        statement = select(Messaging).where(Messaging.id == messaging_id)
        messaging = session.exec(statement).first()
        if not messaging:
            raise HTTPException(status_code=404, detail="Messaging not found")
        session.delete(messaging)
        session.commit()
        return {"message": "Messaging deleted successfully"}
    


@router.put("/messagings/{messaging_id}")
def update_messaging(messaging_id: int, updated_messaging: Messaging):
    with Session(engine) as session:
        statement = select(Messaging).where(Messaging.id == messaging_id)
        messaging = session.exec(statement).first()
        if not messaging:
            raise HTTPException(status_code=404, detail="Messaging not found")
        for key, value in updated_messaging.dict().items():
            setattr(messaging, key, value)
        session.add(messaging)
        session.commit()
        session.refresh(messaging)
        return messaging