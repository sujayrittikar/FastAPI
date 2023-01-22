from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/users')
async def list_users():
    return {'message': 'list users route'}

# Order of Routes matters!

# This is specific route
@app.get('/users/me')
async def get_current_user():
    return {"Message": "This is the current user"}

# This is dynamic route
@app.get('/users/{user_id}')
async def get_user(item_id: int):
    return {'user_id': item_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get('/food/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name==FoodEnum.vegetables:
        return {'food_name': food_name, "message": 'you are healthy'}
    
    if food_name.value=="fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things"
        }
    
    return {"food_name": food_name, "message": "Chocolate milk is really good"}