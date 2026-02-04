
from typing import Dict
from backend.projects.base import BaseProject 
from backend.projects.weather_project import WeatherProject

_PROJECT_REGGISTRY : Dict[str, BaseProject] ={
    "weather" : WeatherProject()
}

def get_project(project_id :str) -> BaseProject:
    if project_id not in _PROJECT_REGGISTRY:
        raise ValueError(f"unknown project_id:{project_id}")
    return _PROJECT_REGGISTRY[project_id]

def list_project():
    """
    used by frontend to show registry page projects.
    """

    return [
        { 
            "project_id": project.project_id,
            "name":project.name,
            "description":project.description,
        }
        for project in _PROJECT_REGGISTRY.values()
    ]