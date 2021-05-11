import random
start = int(input('請輸入起始整數：'))
end = int(input('請輸入終點整數：'))
ans = random.randint(start, end)
times = 0

while True:
    guess = int(input('請猜一個數字：'))
    times = times + 1
    if guess > ans:
        print('你猜的數字比答案大')
    elif guess < ans:
        print('你猜的數字比答案小')
    elif guess == ans:
        print(f'恭喜答對了，答案是{ans}，總共猜了{times}次！')
        break