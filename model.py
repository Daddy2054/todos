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
