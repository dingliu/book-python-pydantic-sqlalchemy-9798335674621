## model with default values
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(default=18, ge=18)
    email: str = Field(default="noreply@example.com")


user = User(name="Default User")
print(user)
