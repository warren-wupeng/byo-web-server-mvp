from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class KnowledgeCard(BaseModel):
    id: str
    title: str
    content: str
    relatedTaskId: str

class Task(BaseModel):
    id: str
    title: str
    description: str
    order: int
    
class TaskDetail(Task):
    codeTemplate: str
    knowledgeCards: List[KnowledgeCard] 