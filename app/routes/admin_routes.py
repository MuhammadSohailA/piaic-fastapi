from fastapi import APIRouter


admin_router = APIRouter( prefix="/api", tags=["admin"])

@admin_router.get("/admin")
def read_admin():
    return {"message": "Hello Admin"}