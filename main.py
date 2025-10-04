from fastapi import FastAPI
from routes import students
from pydantic import BaseModel, EmailStr
app = FastAPI()

name={
    "name":"Rohit",
    "age":24,
    "city":"Indore"
}


# GET REQUEST
@app.get("/")
async def read_root():
    return ({"Message": "Hello Dev! Fast Api Is Working", "Status": "Success"},name)

#Search Paramater or Query Paramater
@app.get("/search")
def search(stdid: int = 16, stdname: str=None):
    return {"Message": "Search Successful", "Status": "Success", "Data": {"id": stdid, "name": stdname}}
#http://localhost:8000/search?stdid=16&stdname=codeboy16



# Add The Routes
app.include_router(students.router)

