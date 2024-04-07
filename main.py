from fastapi import FastAPI, HTTPException
from db import create_db_and_tables, engine
from model import *
from sqlmodel import Session, select

app = FastAPI()

# Call the function to create the database and tables when starting the application
create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Fast API in Python"}
# Functions to add records to each table
@app.post("/persons/")
def create_person(person: Person):
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
        return person

@app.post("/residence_places/")
def create_residence_place(residence_place: ResidencePlace):
    with Session(engine) as session:
        session.add(residence_place)
        session.commit()
        session.refresh(residence_place)
        return residence_place

@app.post("/staff/")
def create_staff(staff: Staff):
    with Session(engine) as session:
        session.add(staff)
        session.commit()
        session.refresh(staff)
        return staff

@app.post("/staff_performances/")
def create_staff_performance(staff_performance: StaffPerformance):
    with Session(engine) as session:
        session.add(staff_performance)
        session.commit()
        session.refresh(staff_performance)
        return staff_performance

@app.post("/customers/")
def create_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

@app.post("/messagings/")
def create_messaging(messaging: Messaging):
    with Session(engine) as session:
        session.add(messaging)
        session.commit()
        session.refresh(messaging)
        return messaging

@app.post("/reservations/")
def create_reservation(reservation: Reservation):
    with Session(engine) as session:
        session.add(reservation)
        session.commit()
        session.refresh(reservation)
        return reservation

@app.post("/rooms/")
def create_room(room: Room):
    with Session(engine) as session:
        session.add(room)
        session.commit()
        session.refresh(room)
        return room

@app.post("/accommodations/")
def create_accommodation(accommodation: Accommodation):
    with Session(engine) as session:
        session.add(accommodation)
        session.commit()
        session.refresh(accommodation)
        return accommodation

@app.post("/additional_services/")
def create_additional_service(additional_service: AdditionalService):
    with Session(engine) as session:
        session.add(additional_service)
        session.commit()
        session.refresh(additional_service)
        return additional_service



    
# Functions to get data from all tables

@app.get("/persons/")
def get_persons():
    with Session(engine) as session:
        statement = select(Person)
        persons = session.exec(statement)
        return persons

@app.get("/residence_places/")
def get_residence_places():
    with Session(engine) as session:
        statement = select(ResidencePlace)
        residence_places = session.exec(statement)
        return residence_places

@app.get("/staff/")
def get_staff():
    with Session(engine) as session:
        statement = select(Staff)
        staff = session.exec(statement)
        return staff

@app.get("/staff_performances/")
def get_staff_performances():
    with Session(engine) as session:
        statement = select(StaffPerformance)
        staff_performances = session.exec(statement)
        return staff_performances

@app.get("/customers/")
def get_customers():
    with Session(engine) as session:
        statement = select(Customer)
        customers = session.exec(statement)
        return customers

@app.get("/messagings/")
def get_messagings():
    with Session(engine) as session:
        statement = select(Messaging)
        messagings = session.exec(statement)
        return messagings

@app.get("/reservations/")
def get_reservations():
    with Session(engine) as session:
        statement = select(Reservation)
        reservations = session.exec(statement)
        return reservations

@app.get("/rooms/")
def get_rooms():
    with Session(engine) as session:
        statement = select(Room)
        rooms = session.exec(statement)
        return rooms

@app.get("/accommodations/")
def get_accommodations():
    with Session(engine) as session:
        statement = select(Accommodation)
        accommodations = session.exec(statement)
        return accommodations

@app.get("/additional_services/")
def get_additional_services():
    with Session(engine) as session:
        statement = select(AdditionalService)
        additional_services = session.exec(statement)
        return additional_services
    


# Functions to delete records from all tables

@app.delete("/persons/{person_id}")
def delete_person(person_id: int):
    with Session(engine) as session:
        statement = select(Person).where(Person.id == person_id)
        person = session.exec(statement).first()
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        session.delete(person)
        session.commit()
        return {"message": "Person deleted successfully"}

@app.delete("/residence_places/{residence_place_id}")
def delete_residence_place(residence_place_id: int):
    with Session(engine) as session:
        statement = select(ResidencePlace).where(ResidencePlace.id == residence_place_id)
        residence_place = session.exec(statement).first()
        if not residence_place:
            raise HTTPException(status_code=404, detail="Residence Place not found")
        session.delete(residence_place)
        session.commit()
        return {"message": "Residence Place deleted successfully"}

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id: int):
    with Session(engine) as session:
        statement = select(Staff).where(Staff.id == staff_id)
        staff = session.exec(statement).first()
        if not staff:
            raise HTTPException(status_code=404, detail="Staff not found")
        session.delete(staff)
        session.commit()
        return {"message": "Staff deleted successfully"}

@app.delete("/staff_performances/{staff_performance_id}")
def delete_staff_performance(staff_performance_id: int):
    with Session(engine) as session:
        statement = select(StaffPerformance).where(StaffPerformance.id == staff_performance_id)
        staff_performance = session.exec(statement).first()
        if not staff_performance:
            raise HTTPException(status_code=404, detail="Staff Performance not found")
        session.delete(staff_performance)
        session.commit()
        return {"message": "Staff Performance deleted successfully"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    with Session(engine) as session:
        statement = select(Customer).where(Customer.person_id == customer_id)
        customer = session.exec(statement).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return {"message": "Customer deleted successfully"}

@app.delete("/messagings/{messaging_id}")
def delete_messaging(messaging_id: int):
    with Session(engine) as session:
        statement = select(Messaging).where(Messaging.id == messaging_id)
        messaging = session.exec(statement).first()
        if not messaging:
            raise HTTPException(status_code=404, detail="Messaging not found")
        session.delete(messaging)
        session.commit()
        return {"message": "Messaging deleted successfully"}

@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    with Session(engine) as session:
        statement = select(Reservation).where(Reservation.id == reservation_id)
        reservation = session.exec(statement).first()
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        session.delete(reservation)
        session.commit()
        return {"message": "Reservation deleted successfully"}

@app.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    with Session(engine) as session:
        statement = select(Room).where(Room.id == room_id)
        room = session.exec(statement).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        session.delete(room)
        session.commit()
        return {"message": "Room deleted successfully"}

@app.delete("/accommodations/{accommodation_name}")
def delete_accommodation(accommodation_name: str):
    with Session(engine) as session:
        statement = select(Accommodation).where(Accommodation.name == accommodation_name)
        accommodation = session.exec(statement).first()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        session.delete(accommodation)
        session.commit()
        return {"message": "Accommodation deleted successfully"}

@app.delete("/additional_services/{additional_service_id}")
def delete_additional_service(additional_service_id: int):
    with Session(engine) as session:
        statement = select(AdditionalService).where(AdditionalService.id == additional_service_id)
        additional_service = session.exec(statement).first()
        if not additional_service:
            raise HTTPException(status_code=404, detail="Additional Service not found")
        session.delete(additional_service)
        session.commit()
        return {"message": "Additional Service deleted successfully"}
    



# Functions to modify records in each table

@app.put("/persons/{person_id}")
def update_person(person_id: int, updated_person: Person):
    with Session(engine) as session:
        statement = select(Person).where(Person.id == person_id)
        person = session.exec(statement).first()
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        for key, value in updated_person.dict().items():
            setattr(person, key, value)
        session.add(person)
        session.commit()
        session.refresh(person)
        return person

@app.put("/residence_places/{residence_place_id}")
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

@app.put("/staff/{staff_id}")
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

@app.put("/staff_performances/{staff_performance_id}")
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

@app.put("/customers/{customer_id}")
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

@app.put("/messagings/{messaging_id}")
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

@app.put("/reservations/{reservation_id}")
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

@app.put("/rooms/{room_id}")
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

@app.put("/accommodations/{accommodation_name}")
def update_accommodation(accommodation_name: str, updated_accommodation: Accommodation):
    with Session(engine) as session:
        statement = select(Accommodation).where(Accommodation.name == accommodation_name)
        accommodation = session.exec(statement).first()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        for key, value in updated_accommodation.dict().items():
            setattr(accommodation, key, value)
        session.add(accommodation)
        session.commit()
        session.refresh(accommodation)
        return accommodation

@app.put("/additional_services/{additional_service_id}")
def update_additional_service(additional_service_id: int, updated_additional_service: AdditionalService):
    with Session(engine) as session:
        statement = select(AdditionalService).where(AdditionalService.id == additional_service_id)
        additional_service = session.exec(statement).first()
        if not additional_service:
            raise HTTPException(status_code=404, detail="Additional Service not found")
        for key, value in updated_additional_service.dict().items():
            setattr(additional_service, key, value)
        session.add(additional_service)
        session.commit()
        session.refresh(additional_service)
        return additional_service
