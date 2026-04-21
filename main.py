from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def fun():
    return {"xd" : "xd"}