from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schema import UserSchema
from docs import tags_metadata

app = FastAPI(
  title="REST API con FastAPI y PostgreSQL",
  description="Esto es una REST API simple utilizando FastAPI y PostgreSQL",
  version="0.0.1",
  openapi_tags=tags_metadata
)
conn = UserConnection()

@app.get("/api/user", status_code=HTTP_200_OK, response_model=list[UserSchema], tags=["users"])
def root():
  items = []
  for data in conn.read_all():
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    items.append(dictionary)
  return items

@app.get("/api/user/{id}", status_code=HTTP_200_OK, response_model=UserSchema, tags=["users"])
def get_one(id:str):
  data = conn.read_one(id)

  dictionary = {}
  dictionary["id"] = data[0]
  dictionary["name"] = data[1]
  dictionary["phone"] = data[2]
  return dictionary

@app.post("/api/user", status_code=HTTP_201_CREATED, tags=["users"])
def insert(user_data:UserSchema):
  data = user_data.dict()
  data.pop("id")
  conn.write(data)
  return Response(status_code=HTTP_201_CREATED)

@app.put("/api/user/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def update(user_data:UserSchema, id:str):
  data = user_data.dict()
  data["id"] = id
  conn.update(data)
  return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete("/api/user/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete(id:str):
  conn.delete(id)
  return Response(status_code=HTTP_204_NO_CONTENT)