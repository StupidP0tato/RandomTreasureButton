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
            <title>Treasure Button</title>
            <style>
                .button {
                    border: none;
                    background: none;
                    cursor: pointer;
                    text-align: center;
                }
                .button img {
                    width: 100px; /* Adjust size as needed */
                    height: auto;
                }
                .text {
                    display: block;
                    margin-top: 10px; /* Spacing between image and text */
                    font-size: 20px; /* Text size */
                }
            </style>
        </head>
        <body>
            <button class="button" onclick="alert('You pressed the treasure!')">
                <img src="/static/ChestSymbol.png" alt="Chest Symbol">
                <span class="text">Treasure</span>
            </button>
        </body>
    </html>
    """

