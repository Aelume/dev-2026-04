# dev-2026-04

## 题目名称

Python 调用 DeepSeek 实现终端流式智能对话

## 这是一道什么题

这道题主要考查：

- Python 基础使用
- `venv` 虚拟环境创建
- API Key 获取与配置
- 环境变量读取
- DeepSeek API 调用
- 终端输入输出
- 流式输出实现
- README 说明能力

本题重点不是做复杂产品，而是看你能不能把一个最基础的命令行智能对话程序写出来。

---

## 如果这是模板仓库，你应该怎么开始

### 第一步：使用模板创建你自己的仓库
在 GitHub 页面点击：

- `Use this template`
- 创建你自己的新仓库

### 第二步：克隆到本地

```bash
git clone <你的仓库地址>
cd <你的仓库名>
```

### 第三步：创建虚拟环境（必须）

请使用 `venv` 创建虚拟环境。

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 第四步：安装依赖

```bash
pip install -r requirements.txt
```

### 第五步：获取并配置 API Key

你需要自己获取 DeepSeek API Key。

然后可以用下面两种方式之一配置：

#### 方式一：设置环境变量

Linux / macOS：

```bash
export DEEPSEEK_API_KEY=你的key
```

Windows PowerShell：

```powershell
$env:DEEPSEEK_API_KEY="你的key"
```

#### 方式二：参考 `.env.example`

你可以自己创建 `.env` 文件，并写入：

```env
DEEPSEEK_API_KEY=你的key
```

### 第六步：修改 `main.py`

本题重点完成：

- `main.py`

---

## 你的任务

你需要完成以下功能：

### 1. 读取 API Key
程序必须通过环境变量读取：

- `DEEPSEEK_API_KEY`

不能把 key 直接写死在代码里。

### 2. 实现终端对话
程序运行后，用户可以：

- 输入问题
- 收到模型回复
- 再继续输入下一轮问题

### 3. 实现流式输出
要求尽量做到“边收到边打印”，而不是整段返回后一次性输出。

### 4. 支持退出
当用户输入下面任意内容时，程序应退出：

- `exit`
- `quit`
- `q`

---

## 运行要求

你的程序至少应该能通过类似下面的方式运行：

```bash
python main.py
```

---

## 提交要求

你需要提交：

1. 完整源码
2. `README.md`
3. `requirements.txt`
4. `.env.example`

注意：

- **不要提交你自己的真实 API Key**
- 只保留 `.env.example`

---

## 评分与验收说明

详细内容请查看：

- [评分细则（面向 agent）](./docs/scoring.md)
- [验收清单](./docs/checklist.md)
- [学生 README 模板](./docs/student-readme-template.md)

---

## 给候选人的说明

这道题不是看你能不能写复杂 AI 产品，而是看你能不能把 API 调用的基础流程接通。

请优先保证：

- 先创建并使用虚拟环境
- 正确获取并配置 API Key
- 程序能正常发起请求
- 能在终端完成流式输出
- 能正常退出

如果你之前没接触过大模型 API，也没关系。先完成最基础版本就可以。