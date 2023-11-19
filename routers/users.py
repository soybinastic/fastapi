from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter(
    prefix='/users'
)


@router.get("/")
def fetch_users():
    return [
        'user 1',
        'user 1',
        'user 1',
        'user 1',
    ]

@router.get("/{id}")
def fetch_users(id):
    return { 'user' :  id}
