from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    Name = Column(Text, nullable=False)
    Last_Name1 = Column(Text, nullable=False)
    Last_Name2 = Column(Text, nullable=False)
    Telephone_Number = Column(Text, nullable=False)
    Cost = Column(Integer, nullable=False)
    Email = Column(Text, nullable=False)
    Number_of_Persons = Column(Integer, nullable=False)
    Check_In = Column(Text, nullable=False)
    Check_Out = Column(Text, nullable=False)
    ID_Room = Column(Integer, ForeignKey('Room.id'), nullable=False)
    ID_Addiccional_Service = Column(Integer, ForeignKey('Addicional_Services.id'), nullable=False)
    ID_Reservation_Data = Column(Integer, ForeignKey('Reservation_Data.id'), nullable=False)
    room = relationship("Room", back_populates="persons")
    addicional_service = relationship("Addicional_Service", back_populates="persons")
    reservation_data = relationship("Reservation_Data", back_populates="persons")

class Reservation_Data(Base):
    __tablename__ = 'Reservation_Data'
    id = Column(Integer, primary_key=True)
    Start_Day = Column(Text, nullable=False)
    Start_Time = Column(Text, nullable=False)
    End_Day = Column(Text, nullable=False)
    End_Time = Column(Text, nullable=False)
    persons = relationship("Person", back_populates="reservation_data")

class Addicional_Services(Base):
    __tablename__ = 'Addicional_Services'
    id = Column(Integer, primary_key=True)
    Name = Column(Text, nullable=False)
    ID_Plans = Column(Integer, ForeignKey('Plans.id'), nullable=False)
    ID_Availability_to_Reserve = Column(Integer, ForeignKey('Availability_to_Reserve.id'), nullable=False)
    plans = relationship("Plans", back_populates="addicional_services")
    availability_to_reserve = relationship("Availability_to_Reserve", back_populates="addicional_services")
    persons = relationship("Person", back_populates="addicional_service")

class Availability_to_Reserve(Base):
    __tablename__ = 'Availability_to_Reserve'
    id = Column(Integer, primary_key=True)
    Day = Column(Text, nullable=False)
    Start_Time = Column(Text, nullable=False)
    End_Time = Column(Text, nullable=False)
    addicional_services = relationship("Addicional_Services", back_populates="availability_to_reserve")

class Plans(Base):
    __tablename__ = 'Plans'
    id = Column(Integer, primary_key=True)
    Name = Column(Text, nullable=False)
    Description = Column(Text, nullable=False)
    Cost = Column(Integer, nullable=False)
    addicional_services = relationship("Addicional_Services", back_populates="plans")

class Accomodation(Base):
    __tablename__ = 'Accomodation'
    Name = Column(Integer, primary_key=True)
    Adminitrative_Code = Column(Text, nullable=False)
    Country = Column(Text, nullable=False)
    City = Column(Text, nullable=False)
    Number_of_Reservations = Column(Integer, nullable=False)
    ID_Room = Column(Integer, ForeignKey('Room.id'), nullable=False)
    ID_Person = Column(Integer, ForeignKey('Person.id'), nullable=False)
    ID_Staff = Column(Integer, ForeignKey('Staff.id'), nullable=False)
    ID_Manager = Column(Integer, ForeignKey('Manager.id'), nullable=False)
    room = relationship("Room", back_populates="accomodations")
    person = relationship("Person", back_populates="accomodations")
    staff = relationship("Staff", back_populates="accomodations")
    manager = relationship("Manager", back_populates="accomodations")

class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    Cost = Column(Integer, nullable=False)
    Number_of_Occupants = Column(Integer, nullable=False)
    Name = Column(Text, nullable=False)
    Services_or_Elements = Column(Text, nullable=False)
    Reserved = Column(Text, nullable=False)
    Discount = Column(Integer, nullable=False)
    Total_Price = Column(Integer, nullable=False)
    accomodations = relationship("Accomodation", back_populates="room")
    persons = relationship("Person", back_populates="room")

class Manager(Base):
    __tablename__ = 'Manager'
    id = Column(Integer, primary_key=True)
    Name = Column(Text, nullable=False)
    Last_Name_1 = Column(Text, nullable=False)
    Last_Name_2 = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    Password = Column(Text, nullable=False)
    Telephone_Number = Column(Text, nullable=False)
    ID_Labor_Data = Column(Integer, ForeignKey('Labor_Data.id'), nullable=False)
    labor_data = relationship("Labor_Data", back_populates="manager")
    accomodations = relationship("Accomodation", back_populates="manager")

class Staff(Base):
    __tablename__ = 'Staff'
    id = Column(Integer, primary_key=True)
    Name = Column(Text, nullable=False)
    Last_Name_1 = Column(Text, nullable=False)
    Last_Name_2 = Column(Text, nullable=False)
    Email = Column(Text, nullable=False)
    Telephone_Number = Column(Text, nullable=False)
    Work_Position = Column(Text, nullable=False)
    ID_Labor_Data = Column(Integer, ForeignKey('Labor_Data.id'), nullable=False)
    labor_data = relationship("Labor_Data", back_populates="staff")
    accomodations = relationship("Accomodation", back_populates="staff")

class Labor_Data(Base):
    __tablename__ = 'Labor_Data'
    id = Column(Integer, primary_key=True)
    Start_Time = Column(Text, nullable=False)
    Day = Column(Text, nullable=False)
    End_Time = Column(Text, nullable=False)
    staff = relationship("Staff", back_populates="labor_data")
    manager = relationship("Manager", back_populates="labor_data")