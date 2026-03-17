"""
需求: 编写一个程序，不断提示用户输入数据，直到输入结束符号“#”。在输入过程中，将用户每次输入的数据
（不包括#）逐行保存到文件中
"""

import os

with open("data.txt","w",encoding = "utf-8") as f:
    while True:
    # 提示用户输入数据
        input_string = input("请输入数据：")
        # 判断
        if input_string == "#":
            print("数据已保存")
            break
        # 将用户输入的数据写入文件
        f.write(input_string + "\n")
