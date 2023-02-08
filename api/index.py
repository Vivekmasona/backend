from fastapi import FastAPI
import dune

app = FastAPI()

@app.get("/")
async def root():
    return {"result": dune.main()}

