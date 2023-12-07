
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/{number}")
def divisibality(number):

    variable = int(number) / 2

    if variable.is_integer() :
        return("even")
    else:
        return("odd")
    


if __name__ == "__main__" :
    uvicorn.run("Homework:app", host= "0.0.0.0", port= 5001, reload=True)
