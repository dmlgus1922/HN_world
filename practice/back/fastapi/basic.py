from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def test():
    return 'test data'

@app.get('/test2')
def test2():
    return 'second page data'

class Model(BaseModel):
    name: str
    email: str
    phonenum: int


@app.post('/send')
def data_receive(data: Model):
    print(data)
    return '전송완료'