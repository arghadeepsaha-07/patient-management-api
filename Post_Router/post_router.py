from fastapi import APIRouter,HTTPException,status,Depends
from Database.database_engine import get_db
from Database.database_models import Patient_Database
from Pydantic.models import Patient_Create,Patient_Response
from sqlalchemy.orm import Session


router = APIRouter(prefix="/CREATE")


@router.post("/create",response_model=Patient_Response)
def create_router(patient:Patient_Create,db:Session=Depends(get_db)):

    db_user = Patient_Database(**patient.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user

