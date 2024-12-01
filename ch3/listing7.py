## class method
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str

    @classmethod
    def create_dummy(cls):
        return cls(name="John Doe", age=33, email="john.doe@exmaple.com")
