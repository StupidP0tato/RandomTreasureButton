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
            <img src="/static/ChestSymbolSmall.png" alt="Chest Symbol">
        </body>
    </html>
    """
