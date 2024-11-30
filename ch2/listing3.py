from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


user = User(name="John Doe", age=22, email="john.doe@example.com")
user_data = user.model_dump_json()
