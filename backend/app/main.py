from fastapi import FastAPI, HTTPException
from typing import List

from app.models.task import Task, TaskDetail, KnowledgeCard

app = FastAPI(title="迷你Web服务器学习应用")

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """获取所有任务列表"""
    pass

@app.get("/api/tasks/{task_id}", response_model=TaskDetail)
async def get_task_detail(task_id: str):
    """获取特定任务的详细信息"""
    pass 