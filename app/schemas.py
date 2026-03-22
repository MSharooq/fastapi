from pydantic import BaseModel

class PostCreate(BaseModel):
    make: str
    model: str