# 学生 README 模板

下面是一份可以直接修改的 README 模板，学生可以直接复制到自己的 `README.md` 中，再按实际情况修改。

# 项目名称

## 项目简介

这是一个使用 Python 调用 DeepSeek API 实现的终端流式对话程序。

## 我完成的内容

- 使用 venv 创建虚拟环境
- 安装依赖
- 通过环境变量读取 API Key
- 调用 DeepSeek API
- 实现终端输入输出
- 实现流式输出
- 支持退出命令

## 运行方式

### 1. 创建虚拟环境

请先创建并激活 `.venv`。

### 2. 安装依赖

安装 `requirements.txt` 中的依赖。

### 3. 配置 API Key

配置 `DEEPSEEK_API_KEY` 环境变量，或者创建 `.env` 文件。

### 4. 运行程序

运行 `python main.py`。

## 实现思路

我通过读取环境变量中的 API Key 调用 DeepSeek 接口，并在终端中实现了流式输出。
