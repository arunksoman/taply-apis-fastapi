from fastapi import APIRouter

router = APIRouter(prefix='/admin')


@router.get('/login')
def admin_login():
    """This API is for Admin Login.
    """
    return {"msg": "admin login"}
