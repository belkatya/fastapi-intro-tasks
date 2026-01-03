from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
def language(language: str = Cookie(default=None)):
    if language is None:
        return {"message": "Language not set"}
    return {"language": language}
# END
