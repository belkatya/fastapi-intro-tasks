from fastapi import FastAPI, Path

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(gt=0)):
    if user_id < 0:
        return 422
    return {"user_id": user_id}
# END
