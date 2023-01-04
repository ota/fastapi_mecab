from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Req(BaseModel):
    text: str

HOST = '0.0.0.0'
PORT = 8000
app = FastAPI()

import MeCab
tagger = MeCab.Tagger()

def mecab(text):
    return tagger.parse(text)

@app.post('/mecab')
def send_result(req:Req):
    result = mecab(req.text)
    return {
        'result': result
    }

if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)
