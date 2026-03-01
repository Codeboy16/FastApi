from fastapi import FastAPI, HTTPException
from schemas import StudentLogin
from database import collection  
from bson import ObjectId

app = FastAPI()

# CREATE
@app.post("/users")
async def create_user(user: StudentLogin):
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

# READ ALL
@app.get("/users")
async def get_users():
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

# READ ONE
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return user
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE
@app.put("/users/{user_id}")
async def update_user(user_id: str, user: StudentLogin):
    result = await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )
    if result.modified_count == 1:
        return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")

# DELETE
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")