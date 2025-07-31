from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
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

@app.get("/{full_path:path}")
def unknown_paths(full_path: str):
    with open("notFound.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=404, media_type="text/html")

class PostModel(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_store: List[PostModel] = []

def serialized_stored_posts():
    posts_converted = []
    for post in posts_store:
        posts_converted.append(post.model_dump())
    return posts_converted

@app.post("/posts")
def create_post(post_payload: List[PostModel]):
    posts_store.extend(post_payload)
    return JSONResponse({"posts": serialized_stored_posts()}, status_code=201)

@app.get("/posts")
def posts_list():
    return JSONResponse({"posts_list": serialized_stored_posts()}, status_code=200)

@app.put("/posts")
def create_or_update_post(post_payload: List[PostModel]):
    global posts_store

    for new_post in post_payload:
        found = False
        for i, existing_post in enumerate(posts_store):
            if new_post.title == existing_post.title:
                posts_store[i] = new_post
                found = True
                break
        if not found:
            posts_store.append(new_post)
    return {"posts": serialized_stored_posts()}
