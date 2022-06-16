from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

app = FastAPI()


# Plain text responses
@app.get("/hello", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"


# JSON responses
@app.get("/hello/json", response_class=JSONResponse)
async def hello_json():
    return {
        "message": "Hello World!"
    }


# HTML responses
@app.get("/hello/html", response_class=HTMLResponse)
async def hello_html():
    content = """
    <html>
        <head>Hello World from Cloud Run!</head>
        <body>Hello World!</body>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)
