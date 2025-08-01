from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

tasks={}

class Task(BaseModel):
    title:str
    completed : bool = False

@app.post("/task/{task_id}")
def crete_task(task_id: int,task:Task):
    if task_id in tasks:
        return {"task is alredy exists"}
    tasks[task_id] = task
    return tasks[task_id]

@app.get("/task/{task_id}")
def get(task_id : int ):
    if task_id in tasks:
        return tasks[task_id]
    return {"student not exists ra punda "}

@app.get("/tasks")
def get():
    return tasks 

@app.put("/update/{task_id}")
def update(task_id : int , task: Task ):
    if task_id not in tasks:
        return {"task not exists "}
    tasks[task_id]=task
    return tasks[task_id]

@app.delete("/delete/{task_id}")
def dele(task_id  : int):
    if task_id not in tasks:
        return { " stduent not exists "}
    del tasks[task_id]
    return {"student deleted succesfully "}



