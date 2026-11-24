# pip install fastapi uvicorn
# uvicorn 14_fastapi:app --reload
# In Swagger UI (/docs), open POST /heroes, click Try it out, and enter:
# {
#     "id": 4,
#     "name": "Python Master",
#     "power": "Coding at Lightning Speed"
# }
# Then open these URLs:
# - API documentation: http://127.0.0.1:8000/docs
# - Welcome page: http://127.0.0.1:8000/
# - All superheroes: http://127.0.0.1:8000/heroes
# - Find Spider-Man: http://127.0.0.1:8000/heroes/2

from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()

# Our superhero database
heroes = [
    {"id": 1, "name": "Superman", "power": "Flying"},
    {"id": 2, "name": "Spider-Man", "power": "Web Shooting"},
    {"id": 3, "name": "Iron Man", "power": "Technology"}
]


# API 1: Welcome message
@app.get("/")
def home():
    return {"message": "Welcome to Superhero World!"}


# API 2: Show all superheroes
@app.get("/heroes")
def get_heroes():
    return heroes


# API 3: Search superhero by ID
@app.get("/heroes/{hero_id}")
def find_hero(hero_id: int):

    for hero in heroes:
        if hero["id"] == hero_id:
            return hero

    return {"message": "Superhero not found!"}


# API 4: Add a new superhero
@app.post("/heroes")
def add_hero(hero: dict):

    heroes.append(hero)

    return {
        "message": "New superhero joined the team!",
        "hero": hero
    }


# API 5: Show a random fun message
@app.get("/fun")
def fun():

    return {
        "message": "You are a Python superhero!",
        "motivation": "Keep Coding, Keep Flying!"
    }
