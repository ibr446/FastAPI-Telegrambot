from pydantic import BaseModel


class UserCreate(BaseModel):
    phone_number: int
    telegram_id: str


class VerifyCode(BaseModel):
    telegram_id: str
    verification_code: str
