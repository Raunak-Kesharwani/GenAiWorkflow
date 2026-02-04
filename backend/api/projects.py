from fastapi import APIRouter
from backend.projects.registry import list_project

router = APIRouter()

@router.get("/projects")
def projects():
    return list_project()
