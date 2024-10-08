import random
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
                    width: 300px; /* Adjust size as needed */
                    height: auto;
                }
                .text {
                    display: block;
                    margin-top: 10px; /* Spacing between image and text */
                    font-size: 20px; /* Text size */
                }
                .result {
                    margin-top: 20px;
                    font-size: 18px;
                    color: #333;
                    font-style: italic;
                }
            </style>
            <script>
                async function getRandomItem() {
                    const response = await fetch('/random-item');
                    const item = await response.text();
                    document.getElementById('result').innerText = item;
                }
            </script>
        </head>
        <body>
            <h1>Press the Treasure Button!</h1>
            <button class="button" onclick="getRandomItem()">
                <img src="/static/ChestSymbol.png" alt="Chest Symbol">
                <span class="text">Treasure</span>
            </button>
            <!-- Div to display the random item -->
            <div id="result" class="result"></div>
        </body>
    </html>
    """

@app.get("/random-item")
async def random_item():
    # Read the randomItems.txt file and return a random line
    with open("randomItems.txt", "r") as file:
        items = file.readlines()
    return random.choice(items).strip()  # Return a random item, removing any extra whitespace
