import os
from tabulate import tabulate

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
# 定义用户名和其对应的密码集合
user_dic = {'zhangshan': '123456', 'lisi': 'asd123', 'wangwu': 'zxc456', 'dengmazi': 'qwe456'}
balance = 0
flag = False
shopping_list = []
# 定义购物数据结构
shopping_date = {'account': {'username': 'zhangshan', 'balance': 0},
                 'shopping_cart': {}}


# 定义函数，功能：查看打印购物记录
def func_print_purchas(dict):
    for key, value in dict.items():
        shopping_list.append([key, value['number'], value['price'] / value['number'], value['price']])
    print(tabulate(shopping_list, headers=('商品', '数量 ', '单价    ', '价格     '), tablefmt='fancy_grid'))
    print('余额：\033[1;47;31m%s\033[0m\n' % balance)


# 定义函数，功能：登陆和返回布尔值
def func_login(username,password):
    while True:
        if user_dic.get(username) == password:
            print('欢迎\033[1;47;31m%s\033[0m！\n您将进入购物商城！' % username)
            return True
        else:
            print('\033[1;47;31m用户名或密码输入错误！\033[0m')
            return False

# 确定用户名和密码输入正确，才能跳出循环
while True:
    username = input('请在此输入您的用户名：').strip()
    password = input('请在此输入您的密码：').strip()
    if func_login(username, password):
        # 如果用户名和密码正确，就把标示为置反
        flag = True
        shopping_date['account']['username'] = username
        break

# 先判断有没有登陆用户的购物数据文件,若果有，打开登录用户的购物数据文件,没有就输入工资余额
if os.path.exists('shopping cart of %s' % username):
    f = open('shopping cart of %s' % username, 'r', encoding='utf-8')
    date = f.read()
    f.close()
    # 处理文件中的数据，把字符串转换成字典
    shopping_date = eval(date)
    # 把数据中的账户余额赋给balance
    balance = shopping_date['account']['balance']
    print('您上一次购物的余额：\033[1;47;31m%s\033[0m' % balance)

    # 询问用户是否要查看上次的购物记录
    while True:
        last_record = input('请确认是否查看上一次的消费记录(输入：y/n)>>').strip()
        if last_record  == 'n':
            print('祝您本次购物愉快！')
            break
        elif last_record == 'y':
            print('您上一次的购物信息'.center(68, '*'))
            func_print_purchas(shopping_date['shopping_cart'])
            print('祝您本次购物愉快！')
            # 显示完购物信息，商品列表归零，防止退出时显示的购物信息重复
            shopping_list = []
            break
        else:
            print('\033[1;47;31m输入错误，请重新输入！\033[0m')
# 第一次购物，也就是没有找到购物记录，执行下面的代码
else:
    while True:
        balance = input('购物前，请在这里输入您的工资：>>').strip()
        if balance.isdigit():
            balance = int(balance)
            shopping_date['account']['balance'] = balance
            print('祝您本次购物愉快！')
            break
        else:
            print('\033[1;47;31m\033[0m工资输入错误，请重新输入！\033[0m')

# 购物程序
while flag:
    # 打印商品列表
    for i, k in enumerate(goods):
        print(i, k['name'], k['price'])
    choice = input('请在这里输入您要购买商品的编号/q(退出)：>>')
    # 如果用户输入的是数字，且在编号内，就把商品加入购物车,并从工资里减去商品价格
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice <= 3:
            if balance >= int(goods[choice]['price']):
                # 已成功选择商品，判断购物车是否有同种商品，有就累加，没有就添加进去
                if shopping_date['shopping_cart'].get(goods[choice]['name']) is None:
                    shopping_date['shopping_cart'][goods[choice]['name']] = {'number': 1,
                                                                             'price': goods[choice]['price']}
                else:
                    shopping_date['shopping_cart'][goods[choice]['name']]['number'] += 1
                    shopping_date['shopping_cart'][goods[choice]['name']]['price'] += goods[choice]['price']

                balance -= goods[choice]['price']
                shopping_date['account']['balance'] = balance
                # 显示工资余额和这一次加入购物车的商品
                print('商品\033[1;47;31m<%s>\033[0m已加入购物车，您的余额：\033[1;47;31m%s\033[0m' % (
                goods[choice]['name'], balance))
            else:
                print('\033[1;47;31m商品价格大于工资余额(%s)，请重新选择商品！\033[0m' % balance)
        else:
            print('\033[1;47;31m\033[0m商品编号错误，请重新输入！\033[0m')
    # 输入q，退出购物，如果购物车有商品，打印商品列表和余额，否则打印没有购物
    elif choice == 'q':
        if shopping_date['shopping_cart']:

            # 调用函数，将购物车的商品信息提取出来，打印成表格显示
            print('您的购物信息'.center(70, '*'))
            func_print_purchas(shopping_date['shopping_cart'])
            print('欢迎下次光临！')
            break
        else:
            print('亲爱的\033[1;47;31m%s\033[0m\n您本次没有购买商品，欢迎下次光临！' % username)
            break
    else:
        print('\033[1;47;31m商品编号错误，请重新输入！\033[0m')

# 将购物数据写入文件
f = open('shopping cart of %s' % username, 'w', encoding='utf-8')
f.write(str(shopping_date))
f.close()
