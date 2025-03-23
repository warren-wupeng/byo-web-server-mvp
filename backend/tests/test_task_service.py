import pytest
from fastapi.testclient import TestClient
from typing import List, Dict

# 导入将要创建的应用和模型
from app.models.task import Task, TaskDetail
from app.main import app

client = TestClient(app)

def test_get_tasks_list():
    """
    测试获取任务列表
    验证:
    1. 返回状态码是否为 200
    2. 返回的数据结构是否正确
    3. 是否包含预期的三个任务（初始化服务器、处理HTTP GET请求、返回静态页面）
    """
    response = client.get("/api/tasks")
    assert response.status_code == 200
    
    tasks: List[Dict] = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) == 3
    
    # 验证任务的基本结构
    first_task = tasks[0]
    assert "id" in first_task
    assert "title" in first_task
    assert "description" in first_task
    assert "order" in first_task
    
    # 验证任务的具体内容
    task_titles = [task["title"] for task in tasks]
    expected_titles = [
        "初始化服务器",
        "处理HTTP GET请求",
        "返回静态页面"
    ]
    assert task_titles == expected_titles
    
    # 验证任务的顺序
    for i, task in enumerate(tasks):
        assert task["order"] == i + 1

def test_get_task_details():
    """
    测试获取单个任务的详细信息
    验证:
    1. 返回状态码是否为 200
    2. 返回的数据结构是否正确
    3. 是否包含任务的完整信息（包括代码模板和知识卡片）
    """
    task_id = "task-1"  # 假设这是第一个任务的ID
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    
    task_detail: Dict = response.json()
    assert isinstance(task_detail, dict)
    
    # 验证任务详情的完整结构
    required_fields = [
        "id",
        "title",
        "description",
        "order",
        "codeTemplate",
        "knowledgeCards"
    ]
    for field in required_fields:
        assert field in task_detail
    
    # 验证第一个任务的具体内容
    assert task_detail["title"] == "初始化服务器"
    assert "socket" in task_detail["description"].lower()
    assert "def" in task_detail["codeTemplate"]  # 确保代码模板包含函数定义
    
    # 验证知识卡片
    knowledge_cards = task_detail["knowledgeCards"]
    assert isinstance(knowledge_cards, list)
    assert len(knowledge_cards) > 0
    
    first_card = knowledge_cards[0]
    assert "id" in first_card
    assert "title" in first_card
    assert "content" in first_card

def test_get_nonexistent_task():
    """
    测试获取不存在的任务
    验证:
    1. 返回状态码是否为 404
    2. 是否返回适当的错误信息
    """
    response = client.get("/api/tasks/nonexistent-task")
    assert response.status_code == 404
    
    error_response = response.json()
    assert "detail" in error_response
    assert "not found" in error_response["detail"].lower() 