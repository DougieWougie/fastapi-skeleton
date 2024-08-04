from fastapi import FastAPI

from web import example, user

app = FastAPI()

# Routers are defined in the web folder
app.include_router(example.router)
app.include_router(user.router)

if __name__ == "__main__":
    """Want a web server to be started when called direct"""
    import uvicorn

    uvicorn.run("main:app", reload=True)
