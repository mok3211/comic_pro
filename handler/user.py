from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/login")
async def login():
    return "success"

@router.post("/register")
async def register():
    return "success"

@router.post("/logout")
async def logout():
    return "success"