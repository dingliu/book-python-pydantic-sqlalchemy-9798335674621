from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(..., gt=18)
    email: str
