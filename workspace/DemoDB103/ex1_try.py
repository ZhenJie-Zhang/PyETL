try:
    c = int(input("[0]剪刀 [1]石頭 [2]布"))
    if c >= 0 and c <= 2:
        print("合理輸入")
    else:
        print("不合理區間")
except ValueError:
    print("你是不是不是輸入整數!")