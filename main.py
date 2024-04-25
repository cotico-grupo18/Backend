from fastapi import FastAPI, HTTPException, APIRouter
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select
from personsController import router as persons_router
from residencePlacesController import router as residence_places_router
from accommodationsController import router as accommodation_controller_router
from staffController import router as staff_controller_router
from staffPerformancesController import router as staff_performances_controller_router
from roomsController import router as rooms_controller_router
from reservationsController import router as reservation_controller_router
from messagingController import router as messaging_controller_router
from customersController import router as customer_controller_router
from addicionalServicesController import router as addicional_services_controller

app = FastAPI()

# Call the function to create the database and tables when starting the application
create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Fast API in Python"}


# Agrupa los routers de cada conjunto de controladores
app.include_router(persons_router, prefix="/persons", tags=["persons"])
app.include_router(residence_places_router, prefix="/residence_places", tags=["residence_places"])
app.include_router(accommodation_controller_router, prefix="/accomodation_controller", tags=["accomodation"])
app.include_router(staff_controller_router, prefix="/staff", tags=["staff"])
app.include_router(staff_performances_controller_router, prefix="/staff_performances", tags=["staff_performances"])
app.include_router(rooms_controller_router, prefix="/rooms", tags=["rooms"])
app.include_router(reservation_controller_router, prefix="/reservation", tags=["reservation"])
app.include_router(messaging_controller_router, prefix="/messaging", tags=["messaging"])
app.include_router(customer_controller_router, prefix="/customer", tags=["customer"])
app.include_router(addicional_services_controller, prefix="/addicional", tags=["addicional"])