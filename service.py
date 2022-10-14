from fastapi import FastAPI
from dbConfig import DataBase

import popular

app = FastAPI()

@app.get("/")
def count():
  setting = ['namedb', 'login', 'password', 'ip/url', port]
  return popular.countProduct(DataBase(*setting))
