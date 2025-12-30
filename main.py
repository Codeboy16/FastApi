from fastapi import FastAPI
from routes import students, teacher, findPg
from pydantic import BaseModel, EmailStr,Field,conint
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

#CROS Allow All Req
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (useful for dev)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# GET REQUEST
@app.get("/")
async def read_root():
    return ({"Message": "Hello Dev! Fast Api Is Working", "Status": "Success",
             "Api Routes": ["/student", "/teacher", "findPg/search?location=gangtok&budget=10000","/findPg/topBestPg","https://findyourpg.onrender.com/findpg"]})





# Add The Routes
app.include_router(students.router)
app.include_router(teacher.router)
app.include_router(findPg.router)
