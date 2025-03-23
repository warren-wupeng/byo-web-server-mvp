# 迷你Web服务器学习应用 - 后端

## 开发环境设置

### 1. 安装 uv

```bash
# 使用 pip 安装 uv
pip install uv

# 或使用 brew（在 macOS 上）
brew install uv
```

### 2. 创建虚拟环境

```bash
# 创建并激活虚拟环境
uv venv
source .venv/bin/activate  # 在 Windows 上使用 .venv\Scripts\activate
```

### 3. 安装依赖

```bash
# 安装生产依赖
uv pip install -e .

# 安装开发依赖（包括测试工具）
uv pip install -e ".[dev]"
```

### 4. 运行测试

```bash
pytest
```

### 5. 运行开发服务器

```bash
uvicorn app.main:app --reload
```

## 项目结构

```
backend/
├── app/
│   ├── main.py          # FastAPI 应用主文件
│   └── models/          # 数据模型
│       └── task.py      # 任务相关模型
├── tests/               # 测试文件
│   └── test_task_service.py
├── pyproject.toml       # 项目配置和依赖管理
└── README.md           # 本文档
```

## 开发指南

1. 添加新依赖：
   ```bash
   uv pip install package-name
   ```

2. 更新依赖：
   ```bash
   uv pip sync
   ```

3. 运行特定测试：
   ```bash
   pytest tests/test_task_service.py -v
   ``` 