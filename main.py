from fastapi import FastAPI

app = FastAPI()

@app.get("/demo")
def read_root():
    return {"Hello": "World"}

@app.get("/demo2")
def read_root2():
    return {"Hello": "World2"}



@app.get("/demo3")
def read_root2():
    return {"Hello": "World3"}