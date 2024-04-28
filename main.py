from fastapi import FastAPI, HTTPException, APIRouter
from db import create_db_and_tables, engine
from model_2 import *
from sqlmodel import Session, select
import uvicorn

# from Controller import*
""" from Controller.persons_controller import router as persons_router
from Controller.accommodations_controller import (
    router as accommodation_controller_router,
)
from Controller.staff_controller import router as staff_controller_router
from Controller.staff_performances_controller import (
    router as staff_performances_controller_router,
)
from Controller.rooms_controller import router as rooms_controller_router
from Controller.reservations_controller import router as reservation_controller_router
from Controller.messaging_controller import router as messaging_controller_router
from Controller.customers_controller import router as customer_controller_router
from Controller.addicional_services_controller import (
    router as addicional_services_controller,
)
 """
app = FastAPI()


# Call the function to create the database and tables when starting the application
create_db_and_tables()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


# Group routers from each set of controllers
""" app.include_router(persons_router, prefix="/persons", tags=["persons"])
app.include_router(
    accommodation_controller_router,
    prefix="/accomodation_controller",
    tags=["accomodation"],
)
app.include_router(staff_controller_router, prefix="/staff", tags=["staff"])
app.include_router(
    staff_performances_controller_router,
    prefix="/staff_performances",
    tags=["staff_performances"],
)
app.include_router(rooms_controller_router, prefix="/rooms", tags=["rooms"])
app.include_router(
    reservation_controller_router, prefix="/reservation", tags=["reservation"]
)
app.include_router(messaging_controller_router, prefix="/messaging", tags=["messaging"])
app.include_router(customer_controller_router, prefix="/customer", tags=["customer"])
app.include_router(
    addicional_services_controller, prefix="/addicional", tags=["addicional"]
) """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
