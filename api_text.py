from pydantic import BaseModel
from api_run import api


class datain(BaseModel):
    text1: str
    text2: str


class dataout(BaseModel):
    append: str
    reverse: str


@api
def text_api(data: datain) -> dataout:
    return dataout(append=data.text1 + data.text2, reverse=data.text2 + data.text1)
