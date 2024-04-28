from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/additional_services/")
def create_additional_service(additional_service: AdditionalService):
    with Session(engine) as session:
        session.add(additional_service)
        session.commit()
        session.refresh(additional_service)
        return additional_service


@router.get("/additional_services/")
def get_additional_services():
    with Session(engine) as session:
        statement = select(AdditionalService)
        additional_services = session.exec(statement).all()
        return additional_services


@router.delete("/additional_services/{additional_service_id}")
def delete_additional_service(additional_service_id: int):
    with Session(engine) as session:
        statement = select(AdditionalService).where(
            AdditionalService.id == additional_service_id
        )
        additional_service = session.exec(statement).first()
        if not additional_service:
            raise HTTPException(status_code=404, detail="Additional Service not found")
        session.delete(additional_service)
        session.commit()
        return {"message": "Additional Service deleted successfully"}


@router.put("/additional_services/{additional_service_id}")
def update_additional_service(
    additional_service_id: int, updated_additional_service: AdditionalService
):
    with Session(engine) as session:
        statement = select(AdditionalService).where(
            AdditionalService.id == additional_service_id
        )
        additional_service = session.exec(statement).first()
        if not additional_service:
            raise HTTPException(status_code=404, detail="Additional Service not found")
        for key, value in updated_additional_service.dict().items():
            setattr(additional_service, key, value)
        session.add(additional_service)
        session.commit()
        session.refresh(additional_service)
        return additional_service
