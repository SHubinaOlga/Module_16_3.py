from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def Get_Users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def Post_Users(username: str = Path(min_length=5, max_length=20, description='Enter Username', example="UrbanUser"),
                    age: int = Path(ge=18, le=80, description='Enter Age', example= "24")) -> str:
    new_user = str(int(max(users, key=int)) +1)
    users[new_user] = f'Имя: {username}, возраст: {age}'
    return f'User {new_user} is registered!'

@app.put("/user/{user_id}/{username}/{age}")
async def Update_User(user_id: str = Path(min_length=1, max_length=1000, description='Enter User ID', example="1"),
                   username: str = Path(min_length=5, max_length=20, description='Enter Username', example="UrbanProfi"),
                   age: int = Path(ge=18, le=80, description='Enter Age', example="28")) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def Delete_User(user_id: str = Path(min_length=1, max_length=1000, description='Enter User ID', example="2")) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted.'

#uvicorn module_16_3:app --reload