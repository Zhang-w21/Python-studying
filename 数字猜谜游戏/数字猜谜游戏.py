import random
import time
target_number = random.randint(0,99)
print("欢迎来到数字猜谜游戏！")
print("我已经想好了一个 0 到 99 之间的数字，来猜猜看吧！")
# 定义开始时间
start_time = time.time()
while True:
    try:
        guess_num = int(input("请输入你的猜测："))
    except ValueError:
        print("请输入一个有效的数字！")
    else:
        # 判断
        if guess_num < target_number:
            print("猜小了！")
        elif guess_num > target_number:
            print("猜大了！")
        else:

            print("恭喜你！猜对了！")
            end_time = time.time()
            break

reaction_time = end_time - start_time
# 提供表现反馈
if reaction_time < 5:
    print(f"反应迅速！只用了{reaction_time:.2f}秒")
elif reaction_time < 10:
    print(f"反应不错！用了{reaction_time:.2f}秒")
else:
    print(f"再接再厉，共用了{reaction_time:.2f}秒")