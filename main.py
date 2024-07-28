from fastapi import FastAPI

from web import example

app = FastAPI()

# Routers are defined in the web folder
app.include_router(example.router)

if __name__ == "__main__":
    """Want a web server to be started when called direct"""
    import uvicorn

    uvicorn.run("main:app", reload=True)