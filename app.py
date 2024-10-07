from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Static Image</title>
        </head>
        <body>
            <h1>Here is the image:</h1>
            <img src="/static/ChestSymbol.png" alt="Chest Symbol">
        </body>
    </html>
    """
