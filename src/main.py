import os
import sys
import difflib
import argparse

# 错误处理
def error_handle(msg):
    print(f"Error: {msg}")
    sys.exit(1)

# 读取文件
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
# 计算文本相似度
def similarity(str1, str2):
    s = difflib.SequenceMatcher(lambda x: x in " \t\n\r.,，。",
                                   str1,
                                   str2)
    return s.ratio()

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

    # 读取文件内容
    try:
        paper = read_file(args.paper_path)
        copied_paper = read_file(args.copied_paper_path)
    except FileNotFoundError as e:
        error_handle(f"{e.filename} not found.")

    # 判断内容是否为空
    if not paper or not copied_paper:
        error_handle("The contents of the file must not be empty.")
    