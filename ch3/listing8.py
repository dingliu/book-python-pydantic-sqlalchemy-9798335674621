# Nested models
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address


user_address = Address(street="this street", city="that city", zipcode="A2B 3C4")
user = User(name="John Doe", age=33, email="john.doe@example.com", address=user_address)
print(user)
