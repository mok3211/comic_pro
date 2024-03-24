from fastapi import APIRouter

router = APIRouter(
    prefix="/uploads",

)

@router.post("/")
async def uploadFile():
    return "success"