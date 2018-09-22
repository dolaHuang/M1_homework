user_dic = {'zhangshan':'123456','lisi':'asd123','wangwu':'zxc456','dengmazi':'qwe456'}  # 定义一个字典，保存用户名和密码
count = 0
username = ''  # 为了可以在写入文件时，可以调用，先定义了username
flag = True

while flag:
    if count < 3:  # 规定最多只能输入3次
        print('您将进行第%s次输入！'%(count+1))  # 提醒用户输入次数。
        while True:  # 判断用户名是否在列表中
            username = input('请在此输入你的用户名：')
            if len(username) == 0:
                print('用户名不能为空!')
            elif user_dic.get(username) is None:
                print('该用户名不存在！')
            else:
                break
        f = open('被锁定用户', 'r', encoding='utf-8')  # 载入被锁定用户文件
        for line in f.readlines():
            if username == line.strip():
                print('该用户名已被锁定,请联系管理员寻求帮助，系统将退出！')
                flag = False  # 如果找到用户名已锁定，将标志位置为反，不进行输入密码操作。
                break
        if flag:  # 如果用户名没有被锁定，就提示输入密码
            password = input('请在此输入您的密码：')
            for key in user_dic:
                if username == key and password == user_dic[key]:
                    print('欢迎使用本系统！\n祝您使用愉快！')
                    flag = False
                    break
                else:  # 输入错误，次数+1
                    print('用户名或密码输入错误！')
                    count += 1
                    break
        f.close()
    else:  # 超过3次 ，锁定用户名
        print('输入错误达到3次，用户名已经被锁定！')
        f = open('被锁定用户','a',encoding='utf-8')
        f.write(username+'\n')
        f.close()
        break




