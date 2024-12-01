## initialization from dict
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


user_data = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}

user = User(**user_data)
