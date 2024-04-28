from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/rooms/")
def create_room(room: Room):
    with Session(engine) as session:
        session.add(room)
        session.commit()
        session.refresh(room)
        return room
    

@router.get("/rooms/")
def get_rooms():
    with Session(engine) as session:
        statement = select(Room)
        rooms = session.exec(statement).all()
        return rooms
    

@router.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    with Session(engine) as session:
        statement = select(Room).where(Room.id == room_id)
        room = session.exec(statement).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        session.delete(room)
        session.commit()
        return {"message": "Room deleted successfully"}
    

@router.put("/rooms/{room_id}")
def update_room(room_id: int, updated_room: Room):
    with Session(engine) as session:
        statement = select(Room).where(Room.id == room_id)
        room = session.exec(statement).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        for key, value in updated_room.dict().items():
            setattr(room, key, value)
        session.add(room)
        session.commit()
        session.refresh(room)
        return room
