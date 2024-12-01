# Initialization from object instance
from pydantic import BaseModel


class OtherUserModel:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email


class User(BaseModel):
    name: str
    age: int
    email: str


other_user = OtherUserModel("John Doe", 33, "john.doe@example.com")
user = User.model_validate(other_user.__dict__)
print(user)
