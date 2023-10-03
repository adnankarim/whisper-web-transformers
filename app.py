from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Serve static files (e.g., JavaScript files)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Read and return an HTML file
    with open("./static/index.html", "r") as file:
        return file.read()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
