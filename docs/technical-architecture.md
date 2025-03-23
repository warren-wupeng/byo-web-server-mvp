# 迷你Web服务器学习应用 - 技术架构设计文档

## 1. 整体架构

本项目采用三层架构设计，包括：
- 前端层（用户界面）
- 后端服务层（业务逻辑）
- AI服务层（智能辅导）
- 代码执行层（沙箱环境）

## 2. 技术栈详细设计

### 2.1 前端层
- **核心框架**
  - React + TypeScript
  - Redux Toolkit（状态管理）
  - Axios（API通信）
  - Socket.io-client（WebSocket通信）

- **UI组件**
  - Material-UI/Ant Design（组件库）
  - Monaco Editor（代码编辑器）
  - React Flow（流程可视化）

### 2.2 后端服务层
- **Web框架**
  - FastAPI（Python）
  - FastAPI WebSocket支持
  
- **数据存储**
  - SQLite（用户进度存储）
  - Redis（可选，用于会话管理）

- **认证授权**
  - JWT（JSON Web Token）

### 2.3 AI服务层
- OpenAI API/其他大模型API集成
- 提示词管理系统
- 上下文管理服务

### 2.4 代码执行层
- Docker容器化环境
- 代码验证服务
- 进程管理系统

## 3. 核心模块设计

### 3.1 模块划分
1. 用户界面模块
2. 任务管理模块
3. 代码编辑模块
4. AI对话模块
5. 代码执行模块
6. 可视化反馈模块

### 3.2 关键接口设计

```typescript
// 任务管理接口
interface TaskAPI {
  getTasks(): Task[];
  getTaskDetails(taskId: string): TaskDetail;
  submitCode(taskId: string, code: string): SubmissionResult;
}

// AI服务接口
interface AIServiceAPI {
  getTaskGuidance(taskId: string): string;
  checkCode(code: string): CodeCheckResult;
  askQuestion(question: string): string;
}

// 代码执行接口
interface CodeExecutionAPI {
  runCode(code: string): ExecutionResult;
  startServer(port: number): ServerStatus;
  stopServer(): void;
}
```

### 3.3 数据模型

```typescript
interface Task {
  id: string;
  title: string;
  description: string;
  order: number;
  codeTemplate: string;
  knowledgeCards: KnowledgeCard[];
}

interface UserProgress {
  userId: string;
  taskId: string;
  status: 'not_started' | 'in_progress' | 'completed';
  code: string;
  lastUpdated: Date;
}

interface KnowledgeCard {
  id: string;
  title: string;
  content: string;
  relatedTaskId: string;
}
```

## 4. 安全设计

### 4.1 代码执行安全
- Docker容器隔离
- 资源使用限制
- 执行超时控制
- 网络访问限制

### 4.2 API安全
- 请求频率限制
- 输入数据验证
- CORS安全配置
- JWT身份认证

## 5. 部署架构

### 5.1 组件部署
- Nginx（反向代理）
- 前端静态资源
- FastAPI后端服务
- AI服务
- Docker沙箱环境
- Redis缓存
- SQLite数据库

## 6. 开发指南

### 6.1 前端开发规范
- 采用组件化开发方式
- 统一状态管理
- 响应式设计适配
- 实现优雅降级

### 6.2 后端开发规范
- 遵循RESTful API设计
- 实现异步处理机制
- 统一错误处理
- 完善的日志系统

### 6.3 AI服务开发规范
- 模板化提示词管理
- 有效的上下文管理
- 实现错误重试机制
- 优化响应缓存

### 6.4 代码执行环境规范
- 实现容器池管理
- 资源监控系统
- 定期清理机制
- 错误追踪系统

## 7. 开发优先级

### 第一阶段（核心功能）
1. 基础任务流程
2. 代码编辑器集成
3. AI代码检查
4. 基本执行环境

### 第二阶段（重要功能）
1. 可视化反馈
2. 知识卡片系统
3. 用户进度管理

### 第三阶段（优化功能）
1. AI实时问答
2. 动画效果
3. 性能优化

## 8. 监控与维护

### 8.1 性能监控
- API响应时间
- 代码执行时间
- 资源使用情况

### 8.2 错误监控
- 异常日志收集
- 用户反馈系统
- 自动告警机制

### 8.3 维护计划
- 定期代码审查
- 安全漏洞扫描
- 性能优化评估 