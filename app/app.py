from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import db, Post

# setup database connection
'''with db:
    db.create_tables([Post])

    # create dummy post
    dummy_post = Post(title="dummy title", body="dummy body")
    dummy_post.save()'''

# setup main router app
app = FastAPI()

# setup templates and static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def post(request: Request):
    return templates.TemplateResponse("index.html", {
                "request": request,
    }) 

@app.get("/{post_id}", response_class=HTMLResponse)
async def post(request: Request, post_id: str):
    return templates.TemplateResponse("post.html", {
                "request": request,
                "post_id": post_id,
    }) 
    


