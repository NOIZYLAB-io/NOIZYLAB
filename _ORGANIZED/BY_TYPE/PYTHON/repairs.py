from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base


class Repair(Base):
    __tablename__ = "repairs"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    action = Column(String)
    status = Column(String)
    notes = Column(String)
