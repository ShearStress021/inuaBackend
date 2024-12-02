from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/users")
async def home() -> dict:
    return {"users": ["obama", "Gracee", "Maryyy"]}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
