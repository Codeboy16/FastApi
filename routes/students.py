from fastapi import APIRouter
from schemas import StudentSchema as User   # Importing the schema as StudentSchema as User for clarity

router = APIRouter()

student=[
    {"id":1,"name":"Rohit","age":24,"city":"Indore"},
    {"id":2,"name":"Rahul","age":25,"city":"Bhopal"},
    {"id":3,"name":"Ramesh","age":26,"city":"Ujjain"}
]

# GET REQUEST
@router.get("/student")
def get_student():
    return student  

@router.get("/student/{id}")
def get_student_id(id: int):
    return student[id-1]

# POST REQUEST
@router.post("/student")
#def add_student(data: dict (data type str)): # Original line accepting a generic dictionary
def add_student(data: User):
    student.append(data)
    return {"Message": "Student Added Successfully", "Status": "Success"}