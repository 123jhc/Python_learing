dict1 = {'张三':123,'李四':321,'王五':101}

def new_user():
    while 1:
        str1 = input('请输入注册账户名:')
        if str1 in dict1.keys():
            print("该用户已存在，请换一个账户名")
        else:
            break
        
    passwd = int(input('账户密码:'))
    dict1[str1] = passwd
    print("注册成功")

def old_user():
    str1 = input("账户名:")
    if str1 not in dict1.keys():
        print("该账户不存在")
    else:
        while 1:
            passwd = int(input("密码:"))
            if passwd == dict1[str1]:
                print("登陆成功")
                break
            else:
                print("密码错误，请重新输入")
            

def show_meum():
    pro = '''
---新建用户:N/n---
---用户登陆:E/e---
---退出程序:Q/q---
请输入指令代码:'''
    while 1:
        print(pro)
        n = input()
        if n == 'N' or n == 'n':
            new_user()
        elif n == 'E' or n == 'e':
            old_user()
        else:
            break

show_meum()


                        
                    
            
        
