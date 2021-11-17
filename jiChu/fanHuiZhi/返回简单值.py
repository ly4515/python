def get_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 调用返回值的函数时，需要有一个变量存储返回值
musician = get_name('jimi', 'hendrix')
print(musician)