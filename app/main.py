from fastapi import FastAPI,Path
from app.routers import stock
# from typing import Optional
# from pydantic import BaseModel
#This is the entry point for FastAPI application. It initializes the app and includes routers
app = FastAPI()

# students = {
#     1:{
#         "name":"Eklavya Nath",
#         "age" : 20,
#         "year" : "20 years old"
#     },
#     2:{
#         "name":"Shourabh Jain",
#         "age" : 30,
#         "year" : "30 years old"
#     }
# }

# class Student(BaseModel):
#     name:str
#     age:int
#     year: str

# class Updatestudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[str] = None
#     year: Optional[str] = None

# @app.get("/")
# def index():
#     return {"name":"First Data"}

# @app.get("/get-student_id/{student_id}")
# def get_student(student_id: int=Path(...,description="Student ID is required",gt=0,lt=5)):
#     return students[student_id]

# @app.get("/get-by-name/{student_id}")
# def get_name(*,student_id:int,name: Optional[str] = None,test:int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#         return {"Data":"Not Found"}
    
# @app.post("/create-student/{student_id}")
# def create_student(student_id:int , student:Student):
#     if student_id in students:
#         return {"Error":"Student Exists"}
    
#     students[student_id] = student
#     return students[student_id]

# @app.put("/update-student/{student_id}")
# def update_student(student_id:int,student:Updatestudent):
#     if student_id not in students:
#         return {"Error":"Student does not exist"}
    
#     if student.name is not None:
#         students[student_id].name = student.name

#     if student.age is not None:
#         students[student_id].age = student.age

#     if student.year is not None:
#         students[student_id].year = student.year

#     # students[student_id] = student
#     return students[student_id]
    
# @app.delete("/delete-student/{student_id}")
# def delete_student(student_id:int):
#     if student_id not in students:
#         return {"Error":"Student does not exist to delete here"}

#     del students[student_id]
#     return {"Message":"Student deleted successfully"} 
#  uvicorn main:app --reload

app.include_router(stock.router)

@app.get("/")
def root():
    return {"message": "Welcome to the stock predictor app"}
