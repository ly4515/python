# 形参指定默认值要放在后面，符合语法，顺序实参才能正确调用
def get_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    # 非空字符串为True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

# 调用返回值的函数时，需要有一个变量存储返回值
musician = get_name('jimi', 'hendrix')
print(musician)
docter = get_name('sdf', 'ko', 'bob')
print(docter)