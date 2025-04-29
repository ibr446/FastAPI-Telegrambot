from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()



@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    code = crud.register_user(db, user.telegram_id, user.phone_number)
    print(f"Verification code for {user.telegram_id}: {code}")
    return {"message": "Verification code sent"}




@app.post("/verify")
def verify(user: schemas.VerifyCode, db: Session = Depends(database.get_db)):
    success = crud.verify_user(db, user.telegram_id, user.verification_code)
    if not success:
        raise HTTPException(status_code=400, detail="Invalid or expired code")
    return {"message": "User successfully verified"}
