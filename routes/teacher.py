from fastapi import APIRouter,Path
from schemas import TeacherSchema   # Importing the schema as TeacherSchema as User for clarity

router =APIRouter()
teacher=[
    {"id":1,"name":"Anil","subject":"Maths","years_of_experience":5},
    {"id":2,"name":"Sunil","subject":"Science","years_of_experience":7},
    {"id":3,"name":"Suresh","subject":"English","years_of_experience":6}
]

# GET REQUEST
@router.get("/teacher")
def get_teacher():
    return teacher
@router.get("/teacher/{id}")
def get_teacher_id(id: int = Path(...,le=10,gt=0)):
    if(id>len(teacher)):
        return {"StatusCode":404,"Status": "Failed","Message": "Teacher Not Found"}
    return teacher[id-1]

# POST REQUEST
@router.post("/teacher")
#def add_teacher(data: dict (data type str)): # Original line accepting a generic dictionary
def add_teacher(data: TeacherSchema):
    teacher.append(data)
    return {"StatusCode":200,"Status": "Success","Message": "Teacher Added Successfully"}

#PUT REQUEST
@router.put("/teacher/{id}")
def update_teacher(id: int, data: TeacherSchema):
    teacher[id-1] = data
    return {"StatusCode":200,"Status": "Success","Message": "Teacher Updated Successfully" }

#Delete Request
@router.delete("/teacher/{id}")
def delete_teacher(id: int):
    teacher.pop(id-1)
    return {"StatusCode":200,"Status": "Success","Message": "Teacher Deleted Successfully"}

