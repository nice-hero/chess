import subprocess
from typing import Optional
import json
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel






app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# request get method url: "/"












@app.get("/")
async def root():
    return {"message": "welcome to my api!!!!ghkuhkljh!!!!!!1"}



@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}






@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published, new_post.rating)
    print(new_post)
    print(new_post.dict())

    return {"data": new_post}







