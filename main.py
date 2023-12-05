from fastapi import FastAPI
import uvicorn

app = FastAPI()

def test():
    print("hello")

@app.get("/")
def root():
    return("hello")

@app.get("/login")
def login():
    return("login")

if __name__ == "__main__" :
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)