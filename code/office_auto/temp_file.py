from tempfile import TemporaryDirectory, TemporaryFile

with TemporaryDirectory() as temp_dir:
    print('文件夹已创建:', temp_dir)

with TemporaryFile(mode='w+') as tmp_file:
    tmp_file.write('文件搬运')
    tmp_file.seek(0)
    data = tmp_file.read()
    print(data)
