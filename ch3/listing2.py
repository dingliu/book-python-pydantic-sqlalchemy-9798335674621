## Model inheritance
from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str


class Student(BaseUser):
    grade: int
