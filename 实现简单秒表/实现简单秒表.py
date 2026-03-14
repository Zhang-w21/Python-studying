# 需求：编写一个程序，实现简单的秒表功能，该程序在用户按下回车键后开始计时，在用户中断程序时停止计时
import time
print("按下回车键开始计时,中断程序则停止计时")
# 等待用户按下回车键以开始计时
input("准备...")

# 定义变量保存计时开始时间
start_time = time.time()
# 打印消息表示计时已经开始
print("开始计时...")
try:
    while True:
        # 计算经过的时间
        elapsed_time = time.time() - start_time
        print(f"\r计时：{elapsed_time:.0f}",end="")
        # 暂停一秒以每秒更新一次显示时：
        time.sleep(1)
except KeyboardInterrupt:
    # 捕捉到用户中断的信号
    # 保存计时计时结束的时间
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f"\n计时结束，总用时{total_time}秒")
