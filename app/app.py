from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from peewee import DoesNotExist

from .database import db, Post

# setup main router app
app = FastAPI()

# setup templates and static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def post(request: Request):
    posts_query = Post.select(Post.id, Post.title) 
    posts = [(p.id, p.title) for p in posts_query]

    return templates.TemplateResponse("index.html", {
                "request": request,
                "posts": posts,
    }) 

@app.get("/{post_id}", response_class=HTMLResponse)
async def post(request: Request, post_id: str):
  
    try:
        post = Post.get_by_id(post_id) 
    except DoesNotExist as e:
        return templates.TemplateResponse("unknown-post.html", {
            "request": request,
            "post_id": post_id,
        })

    return templates.TemplateResponse("post.html", {
                "request": request,
                "post": post,
    }) 
