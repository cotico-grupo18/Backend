from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, ForeignKey

#Creation of classes with their respective attributes according to the needs of each table
class Person(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name1: str
    last_name2: str
    age: int
    gender: str
    email: str
    phone: str
    residence_places: list["ResidencePlace"] = Relationship(back_populates="person")
    customer: Optional["Customer"] = Relationship(back_populates="person")


class ResidencePlace(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    country: str
    city: str
    exact_address: str
    person_id: Optional[int] = Field(foreign_key="person.id")
    person: Optional[Person] = Relationship(back_populates="residence_places")


class Staff(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    position: str
    shift: str
    person_id: Optional[int] = Field(foreign_key="person.id")
    accommodation_id: Optional[str] = Field(foreign_key="accommodation.name")


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
    accommodation_id: Optional[str] = Field(foreign_key="accommodation.name")
    customer_id: Optional[int] = Field(foreign_key="customer.person_id")

class Reservation(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    cost: int
    check_in_date: str
    check_out_date: str
    description: str
    payment_method: str
    customer_id: Optional[int] = Field(foreign_key="customer.person_id")
    accommodation_id: Optional[str] = Field(foreign_key="accommodation.name")
    room_id: Optional[int] = Field(foreign_key="room.id")


class Room(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    typeRoom: str
    status: str


class Accommodation(SQLModel, table=True):
    name: str = Field(primary_key=True)
    cost: int
    typeAcc: str
    amenities: str


class AdditionalService(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    service: str
    availability: str
    accommodation_id: Optional[str] = Field(foreign_key="accommodation.name")
