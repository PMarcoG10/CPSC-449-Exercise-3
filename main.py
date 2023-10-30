from fastapi import FastAPI
from routes import router 
from users_routes import users_router 

app = FastAPI()

app.include_router(router)
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)