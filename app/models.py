from sqlalchemy import Integer, String, Column, ForeignKey, Boolean, DateTime
from database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(Integer, unique=True)
    telegram_id = Column(String, unique=True)
    verification_code = Column(String)
    code_expires_at = Column(DateTime)
    is_verified = Column(Boolean, default=False)

