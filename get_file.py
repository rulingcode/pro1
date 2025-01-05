from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# تعریف کلاس Question با استفاده از Pydantic
class Question(BaseModel):
    parametr1: str
    parametr2: int
    parametr3: bytes

# تعریف کلاس Answer با استفاده از Pydantic
class Answer(BaseModel):
    parametr1: int
    parametr2: bytes

# مسیر POST برای دریافت سوال
@app.post('/question', response_model=Answer)
def receive_question(question: Question):
    # ساخت پاسخ (Answer) به سوال
    answer = Answer(parametr1=200, parametr2=b"Response data")
    return answer
