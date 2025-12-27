from pydantic import BaseModel,Field,StrictStr
from typing import Optional


class StudentLogin(BaseModel):
    email: str
    password: str = Field(..., min_length=8, max_length=20)

class StudentCreate(StudentLogin):
    first_name:StrictStr = Field(..., min_length=2, max_length=20)
    last_name:StrictStr = Field(..., min_length=2, max_length=20)
    #name: use StrictStr insted of str  # won't allow int like 123

class StudentSchema(StudentCreate):
    id: int
    age:int = Field(..., gt=10, lt=100)
    city: str = Field(..., min_length=2, max_length=50)

#Inherient from StudentLogin then StudentCreate then StudentSchema email and password will be there in StudentCreate and StudentSchema

class TeacherSchema(BaseModel):
    id: int
    name: str
    subject: str
    years_of_experience: Optional[int] = 1
    # email: Optional[EmailStr] = None   

#PG Schema
class PgListSchema(BaseModel):
     name:str
     address: str
     price: int
     contact:int
     rating:int

