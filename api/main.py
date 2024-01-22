from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/{number}")
def divisibility(number: int = Path(..., title="The number to check divisibility")):
    variable = number / 2
    if variable.is_integer():
        return {"result": "even"}
    else:
        return {"result": "odd"}

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=5000, reload=True)
