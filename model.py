from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Person(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name1: str
    last_name2: str
    email: str
    phone: str
    number_of_people: int
    price_to_pay: int
    check_in: bool
    check_out: bool

    reservation_date_id: Optional[int] = Field(foreign_key="reservationdate.id")
    reservation_date: Optional["ReservationDate"] = Relationship(back_populates="person")

    additional_service_id: Optional[int] = Field(foreign_key="additionalservice.id")
    additional_service: Optional["AdditionalService"] = Relationship(back_populates="person")

    accommodation_name: int = Field(foreign_key="accommodation.name")
    accommodation: Optional["Accommodation"] = Relationship(back_populates="person")
    

class ReservationDate(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    start_day: str
    start_hour: str
    end_day: str
    end_hour: str
    person: Optional[Person] = Relationship(back_populates="reservation_date")


class Manager(SQLModel, table=True):        
    id: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name1: str
    last_name2: str
    email: str
    phone: str
    password: str

    accommodations: Optional["Accommodation"] = Relationship(back_populates="manager")
    labor_data_id: Optional[int] = Field(foreign_key="labordata.id")
    labor_data: Optional["LaborData"] = Relationship(back_populates="manager")


class LaborData(SQLModel, table=True):        
    id: Optional[int] = Field(primary_key=True)
    day: str
    start_time: str
    end_time: str

    managers: Optional[Manager] = Relationship(back_populates="labor_data")
    staff: Optional["Staff"] = Relationship(back_populates="labor_data")
     


class Staff(SQLModel, table=True):              
    id: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name1: str
    last_name2: str
    position: str
    email: str
    phone: str

    labor_data_id: Optional[int] = Field(foreign_key="labordata.id")
    labor_data: Optional[LaborData] = Relationship(back_populates="staff")
    


class StaffPerformance(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    tasks: str
    description: str
    staff_id: Optional[int] = Field(foreign_key="staff.id")


class Customer(SQLModel, table=True):
    person_id: int = Field(foreign_key="person.id", primary_key=True)
    person: Optional[Person] = Relationship(back_populates="customer")


class Messaging(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    description: str
    date: str
    accommodation_name: Optional[str] = Field(foreign_key="accommodation.name")
    customer_person_id: Optional[int] = Field(foreign_key="customer.person_id")


class Reservation(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    cost: int
    check_in_date: str
    check_out_date: str
    description: str
    payment_method: str
    customer_person_id: Optional[int] = Field(foreign_key="customer.person_id")
    accommodation_name: Optional[str] = Field(foreign_key="accommodation.name")
    room_id: Optional[int] = Field(foreign_key="room.id")


class Room(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    number_occupants: int
    cost: int
    typeRoom: str
    service_elements: str
    reserved: bool
    discount: int
    totalCost: int

    accommodation_name: Optional[str] = Field(foreign_key="accommodation.name")
    accommodation: Optional["Accommodation"] = Relationship(back_populates="room")


class Accommodation(SQLModel, table=True):
    name: str = Field(primary_key=True)
    administrative_code: str
    country: int
    city: str
    number_of_person: int

    manager_id: Optional[int] = Field(foreign_key="manager.id")
    manager: Optional[Manager] = Relationship(back_populates="accommodations")

    staff_id: Optional[int] = Field(foreign_key="staff.id")
    staff: Optional[Staff] = Relationship(back_populates="accommodations")

    room_id: Optional[int] = Field(foreign_key="room.id") 
    room: Optional[Room] = Relationship(back_populates="accommodations")

    persons_id: Optional[int] = Field(foreign_key="person.id") 
    person: Optional[Person] = Relationship(back_populates="accommodations")
    


class AdditionalService(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    service_name: str

    reservation_availability_id: Optional[int] = Field(foreign_key="reservationavailability.id")
    reservation_availability: Optional["ReservationAvailability"] = Relationship(back_populates="additionalServices")

    plans_id: Optional[int] = Field(foreign_key="plans.id")
    plans: Optional["Plans"] = Relationship(back_populates="additional_services")
    
    person_id: Optional[int] = Field(foreign_key="person.id")
    person: Optional["Person"] = Relationship(back_populates="additional_services")
    

class Plans(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str
    cost: str
    additionalService: Optional[AdditionalService] = Relationship(back_populates="plans")


class ReservationAvailability(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    day: str
    start_time: str
    end_time: str
    additionalService: Optional[AdditionalService] = Relationship(back_populates="reservationAvailability")
