import os
import sys
import argparse

# 错误处理
def error_handle(msg):
    print(f"Error: {msg}")
    sys.exit(1)

if __name__ == '__main__':
    # 设置运行参数
    parser = argparse.ArgumentParser(description="论文查重程序")
    parser.add_argument('paper_path', type=str, help="原文文件")
    parser.add_argument('copied_paper_path', type=str, help="抄袭版论文的文件")
    parser.add_argument('result_path', type=str, help="答案文件")
    args = parser.parse_args()

    # 判断是否为绝对路径
    if not all (map(os.path.isabs, vars(args).values())):
        error_handle("All file paths must be absolute paths. Please check the file paths and try again.")