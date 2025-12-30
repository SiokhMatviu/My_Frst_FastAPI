from fastapi import APIRouter

from typing import Annotated
from fastapi import Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskid

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskid:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("/tasks")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
