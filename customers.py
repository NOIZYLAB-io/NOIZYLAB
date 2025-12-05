from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.customers import Customer

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()


@router.post("/")
def create_customer(payload: dict, db: Session = Depends(get_db)):
    customer = Customer(
        name=payload.get("name"),
        email=payload.get("email"),
        phone=payload.get("phone")
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.get("/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return db.query(Customer).filter(Customer.id == customer_id).first()


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    obj = db.query(Customer).filter(Customer.id == customer_id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return {"deleted": True}
