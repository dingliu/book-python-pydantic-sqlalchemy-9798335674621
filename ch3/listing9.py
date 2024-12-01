## Simple validator
from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("age")
    def validate_age(cls, age):
        if age < 18 or age > 65:
            raise ValueError("Age must between 18 and 65")
        return age


valid_user = User(name="John", age=33, email="john@example.com")
print(valid_user)
invalid_user = User(name="Jane", age=17, email="jane@example.com")
print(invalid_user)
