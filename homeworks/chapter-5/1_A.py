from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

con = sqlite3.connect("Students.db", check_same_thread=False)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
   id INT PRIMARY KEY,
   name TEXT,
   groupp TEXT);
""")
con.commit()

class Student(BaseModel):
    id: int
    name: str
    group: str

@app.post("/")
def add_student(student:Student):
    data = (student.id, student.name,student.group)
    cur.execute("INSERT INTO students VALUES(?, ?, ?);", data)
    con.commit()
    return "saved"

@app.put("/")
def update_student(student:Student):
    data = (student.name,student.group, student.id)
    cur.execute("""UPDATE students SET name = ?, groupp = ? WHERE id = ?""", data)
    con.commit()
    return "updated"

@app.get("/{student_id}")
def get_student(student_id:int):
    cur.execute("""SELECT * FROM students WHERE id = ?""", (student_id,))
    record = cur.fetchone()
    return record

@app.get("/")
def get_student():
    cur.execute("""SELECT * FROM students""")
    record = cur.fetchall()
    return record
    
