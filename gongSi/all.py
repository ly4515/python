import paramiko, os, time, zipfile, glob
ip = "152.67.215.232"
user = "root"
passwd = "Ly@1016!"
yaSuoPath = "D:/mine/Docker"  #要压缩的文件夹路径
strZipPath = "D:/mine/zip/"     # 压缩后存放路径
remotePath = "/home/ly/File/"
timelist = time.localtime()
year = str(timelist[0])
month = str(timelist[1])
day = str(timelist[2])
strFileName = year + "_" + month + "_" + day +'.zip' # 压缩包名
cmdstr = strZipPath + strFileName

# 压缩zip包
def zip():
    z = zipfile.ZipFile(cmdstr, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)   # 大文件压缩，默认FALSE
    for dirpath, dirnames, filenames in os.walk(yaSuoPath):
        fpath = dirpath.replace(yaSuoPath, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()

#上传zip到服务器
def upload():
    tran = paramiko.Transport(ip, 22)
    tran.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(tran)
    for dirpath, dirnames, filenames in os.walk(strZipPath):
        fpath = dirpath.replace(yaSuoPath,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            sftp.put(cmdstr, os.path.join(remotePath,filename))
    tran.close()

# 删除本地zip
def remove():
    for file in glob.glob(os.path.join(strZipPath,"*.zip")):
        os.remove(file)
zip()
upload()
remove()
