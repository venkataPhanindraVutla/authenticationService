# File: app/db/init_db.py
from sqlalchemy.orm import Session
from app.db.models.role import Role

def init_db(db: Session):
    if not db.query(Role).first():
        db.add_all([
            Role(name="admin", description="Administrator"),
            Role(name="user", description="Normal User")
        ])
        db.commit()