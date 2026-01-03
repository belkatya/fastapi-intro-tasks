from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/users")
def create_user(username: str = Body(...), email: str = Body(...), age: Optional[int] = Body(None)):
    return {"username": username, "email": email, "age": age, "status": "User created"}
# END
