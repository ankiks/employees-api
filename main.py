from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
person = []

class Person(BaseModel):
    name: str
    post: str
    salary: int
    active: bool = False

@app.post("/person")
def add(p: Person):
    person.append(p)
    return {"message": "Сотрудник добавлен"}

@app.get("/person")
def get_person():
    return {"person": person}

@app.get("/person/{id}")
def get_person_by_id(id: int):
    if id < 0 or id >= len(person):
        return {"error": "Сотрудник не найден"}
    return {"person": person[id]}

@app.put("/person/{person_id}")
def update_note(person_id: int, updated_person: Person):
    if person_id < 0 or person_id >= len(person):
        return {"error": "Сотрудник не найден"}
    person[person_id] = updated_person
    return {"message": "Сотрудник обновлен", "person": updated_person}

@app.delete("/person/{person_id}")
def delete_person(person_id: int):
    if person_id < 0 or person_id >= len(person):
        return {"error": "Сотрудник не найден!"}
    deleted = person.pop(person_id)
    return {"message": "Сотрудник удален", "person": deleted}
