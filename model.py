from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {"examples": [{"id": 1, "item": "Example Schema!"}]}


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "examples": [{"item": "Read the next chapter of the book"}]
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": [{
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }]
        }