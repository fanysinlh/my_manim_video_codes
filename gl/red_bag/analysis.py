import matplotlib.pyplot as plt
from random import random, seed
from time import time

def add_statistics(pm, count, pri_money):
    fruit = [0 for _ in range(pm)]
    nums = []
    for _ in range(count):
        money = pri_money
        for i in range(pm - 1):
            this_num = random()*(2 * money/(pm - i))
            nums.append(this_num)
            money -= this_num
        nums.append(money)
        max_index = nums.index(max(nums))
        nums = []
        fruit[max_index] += 1
    return fruit

def main():
    # 指定中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题
    seed(time())
    for i in range(2, 13):
        fruit = add_statistics(i, 1000000, 10)
        print(fruit)
        x = range(1, i + 1)
        plt.xticks(x)
        plt.xlabel("抢红包顺序")
        plt.ylabel("获得钱数")
        plt.plot(x, fruit)
        plt.savefig(f"pictures/{i}.png", dpi=300, bbox_inches='tight', transparent=True)
        plt.clf()

if __name__ == "__main__":
    main()