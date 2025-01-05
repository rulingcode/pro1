from pydantic import BaseModel
from api_run import api


class datain(BaseModel):
    num1: int
    num2: int


class dataout(BaseModel):
    sum: int
    product: int


@api
async def calculate(numbers: datain) -> dataout:
    sum_result = numbers.num1 + numbers.num2
    product_result = numbers.num1 * numbers.num2
    return dataout(sum=sum_result, product=product_result)

