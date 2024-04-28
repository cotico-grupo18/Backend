from typing import Optional, List
from sqlmodel import SQLModel, Field, ForeignKey, Relationship

class Person(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Name: str
    Last_Name1: str
    Last_Name2: str
    Telephone_Number: str
    Cost: int
    Email: str
    Number_of_Persons: int
    Check_In: str
    Check_Out: str
    ID_Room: int = Field(foreign_key="Room.id")
    ID_Addiccional_Service: int = Field(foreign_key="Addicional_Services.id")
    ID_Reservation_Data: int = Field(foreign_key="Reservation_Data.id")

    room: Optional["Room"] = Relationship(back_populates="persons")
    addicional_service: Optional["Addicional_Services"] = Relationship(back_populates="persons")
    reservation_data: Optional["Reservation_Data"] = Relationship(back_populates="persons")

class Reservation_Data(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Start_Day: str
    Start_Time: str
    End_Day: str
    End_Time: str

    persons: List["Person"] = Relationship(back_populates="reservation_data")

class Addicional_Services(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Name: str
    ID_Plans: int = Field(foreign_key="Plans.id")
    ID_Availability_to_Reserve: int = Field(foreign_key="Availability_to_Reserve.id")

    persons: List["Person"] = Relationship(back_populates="addicional_service")

class Availability_to_Reserve(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Day: str
    Start_Time: str
    End_Time: str

class Plans(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Name: str
    Description: str
    Cost: int

class Room(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Cost: int
    Number_of_Occupants: int
    Name: str
    Services_or_Elements: str
    Reserved: str
    Discount: int
    Total_Price: int

    persons: List["Person"] = Relationship(back_populates="room")

class Manager(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Name: str
    Last_Name_1: str
    Last_Name_2: str
    Email: str
    Password: str
    Telephone_Number: str
    ID_Labor_Data: int = Field(foreign_key="Labor_Data.id")

class Staff(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Name: str
    Last_Name_1: str
    Last_Name_2: str
    Email: str
    Telephone_Number: str
    Work_Position: str
    ID_Labor_Data: int = Field(foreign_key="Labor_Data.id")

class Labor_Data(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    Start_Time: str
    Day: str
    End_Time: str
