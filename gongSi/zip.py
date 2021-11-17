import time,zipfile
class zip:
    def get_zip(self,files,zip_name):
        zp=zipfile.ZipFile(zip_name,'w', zipfile.ZIP_DEFLATED)
        for file in files:
            zp.write(file)
        zp.close()
        time.sleep(5)
        print('压缩完成')

if __name__ == '__main__':
    z=zip()
    # 文件的位置，多个文件用“，”隔开
    files=['./report.html','./report.txt']
    # 压缩包路径及名字
    zip_file = './66.zip'
    z.get_zip(files,zip_file)