from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

"""
    Path Parameter: Path which the request is using
        Ex: news.com/questions -> /questions is the end point the request is referring to
    Query Parameter: Specific Query to be found or used on the end point or direct domain
        Ex: news.com/questions?sort=Newest > sort=Newest specifies the specific way of querying the data
"""

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

# Home Page
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    if student_id in students.keys():
        return students[student_id]
    else:
        return {
            "Invalid Student ID"
        }

# Path + Query Parameters
@app.get("/get-by-name/{student_id}")
def get_student(
    *,
    student_id: int,
    name: Optional[str] = None,
    test: int = 0
) -> dict:
    if student_id not in students.keys():
        return {
            "Invalid Student ID"
        }

    student = students[student_id]

    if student['name']==name:
        return student
    
    return {
        "Student Name Not Found"
    }

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]