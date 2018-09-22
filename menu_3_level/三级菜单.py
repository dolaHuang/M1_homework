menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

# 定义函数，提示用户输入想查看的目录


def choice(dic):
    while True:
        for key in dic:
            print(key)
        y_choice = input('在这里输入你想查看的目录>:')
        if y_choice in dic.keys():
            if not dic[y_choice]:
                print('%s没有下级目录'%y_choice)
                return 'q'
            ret = choice(dic[y_choice])  # 写递归调用自己，设置变量为了给返回时调用
            if ret == 'q':
                return 'q'  # 把q 返回给上一次层
        elif y_choice == 'q'or y_choice == 'b':
            return y_choice  # 把输入返回给上一层
choice(menu)  # 调用函数，来执行功能
