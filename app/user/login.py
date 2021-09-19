from fastapi import APIRouter
from .model import User

router = APIRouter()


@router.get('/login', tags=['admin'])
async def login_admin():
    User()
    return {"msg": "Success"}