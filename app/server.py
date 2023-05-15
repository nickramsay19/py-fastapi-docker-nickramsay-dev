import uvicorn
from .app import app

def start():
    uvicorn.run("app.app:app", host="0.0.0.0", port=80, reload=True)
