from fastapi import APIRouter, HTTPException
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select

router = APIRouter()


@router.post("/customers/")
def create_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer


@router.get("/customers/")
def get_customers():
    with Session(engine) as session:
        statement = select(Customer)
        customers = session.exec(statement).all()
        return customers


@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.person_id == customer_id)
        customer = session.exec(statement).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return {"message": "Customer deleted successfully"}


@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_customer: Customer):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.person_id == customer_id)
        customer = session.exec(statement).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        for key, value in updated_customer.dict().items():
            setattr(customer, key, value)
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer
