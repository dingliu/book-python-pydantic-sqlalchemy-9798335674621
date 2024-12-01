## initialization from JSON data
import json
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


json_data = '{"name": "John Doe", "age": 30, "email": "john.doe@example.com"}'

user = User.model_validate_json(json_data)
print(user)
