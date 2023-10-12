from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status
import random

app = FastAPI()


class InputData(BaseModel):
    sentence: str


# Function to generate a random 500-dimensional array of floats
def generate_random_array():
    return [random.uniform(0, 1) for _ in range(500)]


# API endpoint to receive a sentence as input and return the random array
@app.post("/generate_array/", status_code=status.HTTP_201_CREATED)
async def generate_array(data: InputData):
    # Validate input using Pydantic
    sentence = data.sentence
    if not sentence:
        raise HTTPException(status_code=400, detail="Input sentence cannot be empty")

    # Generate the random array
    random_array = generate_random_array()

    return {"input_sentence": sentence, "random_array": random_array}
