import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# 当对话历史超过此轮数时，触发压缩
MAX_ROUNDS = 10

SYSTEM_PROMPT = "你是一个有帮助的助手。"


def compress_history(client, messages):
    """把较长的历史对话压缩成摘要，失败时返回 None。"""
    summary_request = [
        {
            "role": "system",
            "content": "请用中文简要总结以下对话的要点，保留关键信息，方便后续继续对话。",
        },
        {
            "role": "user",
            "content": "\n".join(
                f"{m['role']}: {m['content']}" for m in messages if m["role"] != "system"
            ),
        },
    ]

    try:
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=summary_request,
        )
        summary = resp.choices[0].message.content
    except Exception:
        return None

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": f"以下是之前对话的摘要：\n{summary}"},
    ]


def main():
    # 加载 .env 文件（如果存在）
    load_dotenv()

    # 读取 API Key
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("错误：未找到 DEEPSEEK_API_KEY 环境变量。")
        print("请设置环境变量或在 .env 文件中配置。")
        sys.exit(1)

    # 初始化 OpenAI 客户端，指向 DeepSeek API
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )

    # 对话历史
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

    print("DeepSeek 终端对话（输入 exit / quit / q 退出）")
    print("-" * 40)

    while True:
        # 获取用户输入
        try:
            user_input = input("\n你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        # 退出判断
        if user_input.lower() in ("exit", "quit", "q"):
            print("再见！")
            break

        # 跳过空输入
        if not user_input:
            continue

        request_messages = messages + [{"role": "user", "content": user_input}]
        assistant_reply = ""

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=request_messages,
                stream=True,
            )

            print("\nAI: ", end="", flush=True)

            for chunk in response:
                delta = chunk.choices[0].delta
                if delta.content:
                    print(delta.content, end="", flush=True)
                    assistant_reply += delta.content

            print()

            messages = request_messages
            messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            print(f"\n请求出错：{e}")
            if assistant_reply:
                print("本轮回复未完整返回，这一轮不会写入对话历史。")

        user_count = sum(1 for m in messages if m["role"] == "user")
        if user_count >= MAX_ROUNDS:
            print("\n[系统] 对话较长，正在压缩上下文...")
            compressed_messages = compress_history(client, messages)
            if compressed_messages is None:
                print("[系统] 压缩失败，已保留原始上下文。\n")
            else:
                messages = compressed_messages
                print("[系统] 压缩完成，可以继续对话。\n")


if __name__ == "__main__":
    main()
