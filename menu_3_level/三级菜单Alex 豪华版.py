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

current_dir = menu
last_dirs = []
choice = ''

while True:
    # 如果current_dir 不是空的，将列出当前目录
    if current_dir:
        for key in current_dir:
            print(key)
        choice = input('在这里输入你想查看的目录（退出输入q）：>>')
        if not choice:continue
        elif choice in current_dir:
            last_dirs.append(current_dir)
            current_dir = current_dir[choice]
        elif choice == 'b':
            # 如果last_dirs，表示这里是顶层，把当前目录赋给last_dirs，并提示这是顶层目录
            if last_dirs:
                current_dir = last_dirs
            else:print('这是顶层目录！')
        elif choice == 'q':
            exit('感谢您使用本系统')
            # 如果current_dir 不是空的，将提示这是底层
    else:
        print('%s这是底层下面没有目录！'%choice)
        current_dir = last_dirs.pop()
