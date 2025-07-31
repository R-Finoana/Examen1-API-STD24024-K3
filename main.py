from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

app = FastAPI()

@app.get("/ping")
def get_ping(request: Request):
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.get("/home")
def welcome_user(request: Request):
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return Response(content=html_content, status_code=200, media_type="text/html")

@app.post("/")
def create_post():
    return {"message":f"Hello"}

@app.put("/")
def put_update():
    return Response({"message": "Update recorded successfully !"}, status_code=200)
