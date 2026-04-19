# DeepSeek 终端对话小工具

## 项目简介

这是一个很基础的命令行对话程序，用 Python 调用 DeepSeek API，在终端里边收边打印回复。

程序支持：

- 从环境变量或 `.env` 读取 `DEEPSEEK_API_KEY`
- 在终端里连续提问
- 流式输出模型回复
- 输入 `exit`、`quit` 或 `q` 退出
- 对话太长时自动做一次摘要，避免上下文越来越大

## 运行方式

### 1. 创建并激活虚拟环境

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

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

可以参考 `.env.example` 新建一个 `.env` 文件：

```env
DEEPSEEK_API_KEY=你的key
```

也可以直接设置环境变量：

```bash
# Linux / macOS
export DEEPSEEK_API_KEY=你的key

# Windows PowerShell
$env:DEEPSEEK_API_KEY="你的key"
```

### 4. 运行程序

```bash
python main.py
```

## 说明

代码放在 `main.py`，依赖写在 `requirements.txt`。

整体实现比较直接：

1. 启动时加载 `.env`
2. 读取 `DEEPSEEK_API_KEY`
3. 进入循环，接收用户输入
4. 调用 DeepSeek 接口并流式打印结果
5. 把每轮成功的问答保存到历史里

如果连续对话很多轮，程序会把旧对话压缩成一段摘要，再继续后面的聊天。

## 效果展示

![效果展示](assets/屏幕截图%202026-04-20%20013048.png)
