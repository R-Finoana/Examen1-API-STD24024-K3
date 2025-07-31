from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

app = FastAPI()

@app.get("/ping")
def get_ping(request: Request):
    return Response(content="pong", status_code=200, media_type="text/plain")


@app.post("/")
def create_post():
    return {"message":f"Hello"}

@app.put("/")
def put_update():
    return Response({"message": "Update recorded successfully !"}, status_code=200)
