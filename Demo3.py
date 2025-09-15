# 文件名：hello_vscode.py
# 作用：问好 + 计算 1..5 的平方 + 写入本地文件

import sys
import platform
from datetime import datetime

def square(n: int) -> int:
    return n * n

def main():
    name = input("你的名字（可直接回车跳过）：").strip() or "开发者"
    print(f"Hello, {name}! 来自 VS Code ✅")

    nums = list(range(1, 6))
    squares = [square(x) for x in nums]
    print("1..5 的平方：", squares)

    # 把结果写到工作区的文本文件里
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(f"生成时间: {datetime.now()}\n")
        f.write("平方结果: " + ",".join(map(str, squares)) + "\n")

    print("已写入文件：results.txt")
    print("Python 版本：", sys.version.split()[0], "| 操作系统：", platform.platform())

if __name__ == "__main__":
    main()
