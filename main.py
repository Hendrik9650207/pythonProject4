import random


trans = ["剪刀", "石頭", "布"]
file = open("record.txt", "w", encoding="utf-8")
n = 1
win = 0
lose = 0
tie = 0

while True:
    try:
        me = int(input("請出拳 [0]剪刀 [1]石頭 [2]布"))

        com = random.randint(0, 2)

        # 清單名字[號碼牌]

        print("你出的:", trans[me])
        print("對手:", trans[com])

        if me == com:
            print("平手")
            tie += 1
            file.write(str(n))
            file.write(" 平手\n")
        elif me == (com + 1) % 3:
            print("我贏了")
            win += 1
            file.write(str(n))
            file.write(" 我贏了\n")
        else:
            print("我輸了")
            lose += 1
            file.write(str(n))
            file.write(" 我贏了\n")
        # n += 1

    except (IndexError, ValueError):
        print("請輸入0到2")

