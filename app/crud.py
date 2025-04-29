from sqlalchemy.orm import Session
from app.models import User
from datetime import datetime, timedelta
import random



def generate_code():
    return str(random.randint(100000, 999999))

def register_user(db: Session, telegram_id: int, phone_number: str):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    code = generate_code()
    expires_at = datetime.utcnow() + timedelta(minutes=1)

    if user:
        user.phone_number = phone_number
        user.verification_code = code
        user.expires_at = expires_at
        user.is_verified = False
    else:
        user = User(
            telegram_id=telegram_id,
            phone_number=phone_number,
            verification_code=code,
            expires_at=expires_at,
            is_verified=False
        )
        db.add(user)

    db.commit()
    db.refresh(user)
    return code

def verify_user(db: Session, telegram_id: int, verification_code: str):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        return False
    if user.verification_code != verification_code:
        return False
    if datetime.utcnow() > user.expires_at:
        return False

    user.is_verified = True
    db.commit()
    return True