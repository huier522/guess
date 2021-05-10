import random
ans = random.randint(1, 100)
times = 0

while True:
    guess = int(input('1~100 請猜一個數字：'))
    times = times + 1
    if guess > ans:
        print('你猜的數字比答案大')
    elif guess < ans:
        print('你猜的數字比答案小')
    elif guess == ans:
        print(f'恭喜答對了，答案是{ans}，總共猜了{times}次！')
        break