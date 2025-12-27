from fastapi import FastAPI
from routes import students, teacher, findPg
from pydantic import BaseModel, EmailStr,Field,conint
app = FastAPI()


# GET REQUEST
@app.get("/")
async def read_root():
    return ({"Message": "Hello Dev! Fast Api Is Working", "Status": "Success",
             "Api Routes": ["/student", "/teacher", "/search"]})





# Add The Routes
app.include_router(students.router)
app.include_router(teacher.router)
app.include_router(findPg.router)
