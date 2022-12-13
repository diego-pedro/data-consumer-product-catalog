"""Login implementation."""

from fastapi import APIRouter
from services.data_management import authenticate_user
from schemas.user import Authentication

router = APIRouter(tags=["Login API"])

# router -> Interface of Service
@router.post("/login")
async def authenticate(auth: Authentication):
    return authenticate_user(username=auth.username,
                             password=auth.password)
