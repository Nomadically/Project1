from fastapi import FastAPI
from . import models
from .database import engine
from .config import settings
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# below not needed once alembic installed/good to go
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = [
#     "https://www.google.com",
#     "https://www.youtube.com"
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "welcome to my api!!@"}

"""
DO NOT EVER LOAD INTO GIT --- ADD THIS TO GITIGNORE
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

"""

