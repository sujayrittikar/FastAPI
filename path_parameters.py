from fastapi import FastAPI

app = FastAPI()

"""
    Path Parameter: Path which the request is using
        Ex: news.com/questions -> /questions is the path the request is referring to
    Query Parameter: Specific Query to be found or used on the path or direct domain
        Ex: news.com/questions?sort=Newest > sort=Newest specifies the specific way of querying the data
"""

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

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