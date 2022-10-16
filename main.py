from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = []

@app.get("/")
async def root(cookies: str):
    fake_items_db.append(cookies)
    return {"message": "Thanks for ur cookie m8"}

@app.get("/items")
async def read_item():
    return fake_items_db

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")