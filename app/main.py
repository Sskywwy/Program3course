from fastapi import FastAPI, APIRouter
from app.api.v1.router import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")



    
@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)