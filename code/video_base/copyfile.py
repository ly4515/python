import os
# 将指定文件夹下的所有文件复制到其他文件夹
old_path = 'D:\\mine\\Python\\old_path'
new_path = 'D:\\mine\\Python\\new_path'


def copy(old_path, new_path):
    # 判断所给参数是否为文件夹
    if not os.path.isdir(old_path) and os.path.isdir(new_path):
        print('not dir')
    # 判断目标目录是否存在，不存在创建
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        print('目录不存在，已创建')

    # 获取指定文件夹下所有文件
    filelists = os.listdir(old_path)
    # 遍历文件
    for file in filelists:
        # 读文件
        file1 = os.path.join(old_path, file)
        with open(file1, 'rb') as f:
            fr = f.read()
            # 写文件
            file2 = os.path.join(new_path, file)

            with open(file2, 'wb') as f:
                f.write(fr)

    print('复制完成！')


copy(old_path, new_path)

# 复制包含文件夹（递归）
