from fastapi import APIRouter,HTTPException
from pydantic import BaseModel, EmailStr,Field,conint
import random
router = APIRouter()
import json
with open('data.json', 'r') as file:
    pgList = json.load(file)

#Get All PG Details
@router.get("/findpg")
async def PgData():
     random.shuffle(pgList)
     return pgList

#Top 5 Best Pg Gangtok
@router.get("/findPg/topBestPg")
async def topBestPg():
    sortedPgList = [pg for pg in pgList if pg['rating'] >=4 or pg['rating'] == 5 ]
    top_5_pg = random.sample(sortedPgList, 5) if len(sortedPgList) >= 5 else sortedPgList
    return top_5_pg

#Search Paramater or Query Paramater
@router.get("/findPg/search")
def search(location: str, budget:conint(ge=1000,le=30000),status_code=200):
    sortedPgSearch = [pg for pg in pgList if pg['price'] <= budget and location.lower() in pg['address'].lower()]
    if(sortedPgSearch):
      return sortedPgSearch
    raise HTTPException(status_code=404, detail="Item not found")


#http://localhost:8000/findPg/search?location="gangtok"&budget=10000
