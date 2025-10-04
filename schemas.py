from pydantic import BaseModel, EmailStr
from typing import Optional


class StudentSchema(BaseModel):
    id: int
    name: str
    age:int
    city: str
    # email: Optional[EmailStr] = None
