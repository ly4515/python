import shutil
old_path = 'D:/mine/Python/python/code/gongSi'
new_path = 'D:/mine/Python/python/code/office_auto/gongSi'
# shutil.copy('D:/mine/Python/python/code/office_auto/mk_rm_dir.py','D:/mine/Python/python/code/office_auto/pack')

# shutil.copytree('D:/mine/Python/python/code/Reptile', 'D:/mine/Python/python/code/office_auto/office')

shutil.move(old_path, new_path)
