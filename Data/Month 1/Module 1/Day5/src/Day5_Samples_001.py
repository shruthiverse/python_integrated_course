
---

### Code Sample for Day 5
Below is a single Python file (`Day5_Samples_001.py`) with five sample programs tailored to Module 5: API Development (Days 21-25), focusing on Day 5's topics of REST API basics and endpoint creation with FastAPI. Note that this requires running with `uvicorn` and assumes a development environment.

```python
# Day5_Samples_001.py
# Program 1: Basic FastAPI Setup
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Day 5 API!"}

# Program 2: Simple GET Endpoint with Path Parameter
@app.get("/greet/{name}")
async def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}

# Program 3: Endpoint with Query Parameter
@app.get("/info")
async def get_info(age: int):
    return {"age_info": f"You are {age} years old."}

# Program 4: Endpoint Returning a List
@app.get("/users")
async def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return {"users": users}

# Program 5: POST Endpoint (Example with Data)
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"item_added": item.name, "price": item.price}