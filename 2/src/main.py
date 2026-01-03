from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
def filter(min: int = Query(default=0, ge=0, le=100), max: int = Query(default=100, ge=0, le=100)):
    if min < 0 or max > 100 or min > max or max < min:
        return 422
    return {"min": min, "max": max}
# END
