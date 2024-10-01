from fastapi import FastAPI

app = FastAPI()

@app.get("/demo")
def read_root():
    return {"Hello": "World"}