# 先設定好密碼 a123456
# 使用者最多輸入3次
# 不對的話 ，輸出 密碼錯誤，還有＿次機會
# 對的話 印出登入成功

password = 'a123456'
time = 3

while True:
    user = input('請輸入密碼：')
    if user == password:
        print('登入成功')
        break
    else:
        time -= 1
        if time == 0:
            break
        else:
            print(f'輸入錯誤，你還有{time}次機會')
