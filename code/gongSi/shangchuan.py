import paramiko, time, os
strCVSPath = "D:/mine/Docker"  #要压缩的文件夹路径
strZipPath = "D:/mine/zip/"     # 压缩后存放路径
timelist = time.localtime()
year = str(timelist[0])
month = str(timelist[1])
day = str(timelist[2])
strFileName = year + "_" + month + "_" + day +'.zip' # 压缩包名
cmdstr = strZipPath + strFileName

#上传文件到服务器
def upload():
    tran = paramiko.Transport("152.67.215.232", 22)
    tran.connect(username="root", password="Ly@1016!")
    sftp = paramiko.SFTPClient.from_transport(tran)
    remoterpath = "/home/ly/File/"
    for dirpath, dirnames, filenames in os.walk(strZipPath):
        fpath = dirpath.replace(strCVSPath,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            sftp.put(cmdstr, os.path.join(remoterpath,filename))
    tran.close()
upload()