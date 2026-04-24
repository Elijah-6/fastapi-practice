from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")

posts: list[dict[str, str]] = [
    {"id": "1", "title": "First Post", "content": "This is the first post."},
    {"id": "2", "title": "Second Post", "content": "This is the second post."},
    {"id": "3", "title": "Third Post", "content": "This is the third post."},
]

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home Page"})

@app.get("/posts/{post_id}")
async def read_post(request: Request, post_id: str):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        return templates.TemplateResponse(request, "404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse(request, "post.html", {"request": request, "post": post})


