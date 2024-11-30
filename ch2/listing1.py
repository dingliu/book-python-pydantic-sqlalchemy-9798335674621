from pydantic import BaseModel


# a basic model
class User(BaseModel):
    name: str
    age: int
    email: str
