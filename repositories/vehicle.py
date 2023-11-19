
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

models.Base.metadata.create_all(bind=engine)

def fetch_all_vehicles():
    db : Session = SessionLocal()
    return db.query(models.Vehicle).all()