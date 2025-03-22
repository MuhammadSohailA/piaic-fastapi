from database import init_db
from models.user_model import Users
from routes.admin_routes import admin_router
from routes.user_routes import user_router

from fastapi import FastAPI

app = FastAPI()


# postgresql , psycopg2

# user routes
app.include_router(admin_router)

#  user routes
app.include_router(user_router)


@app.on_event("startup")
async def on_startup():
    await init_db()
