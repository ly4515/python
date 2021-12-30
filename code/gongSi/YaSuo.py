import os, time, zipfile
strCVSPath = "D:/mine/Docker"  #要压缩的文件夹路径
strZipPath = "D:/mine/zip/"     # 压缩后存放路径
timelist = time.localtime()
year = str(timelist[0])
month = str(timelist[1])
day = str(timelist[2])
strFileName = year + "_" + month + "_" + day +'.zip' # 压缩包名
cmdstr = strZipPath + strFileName

def zip():       # 压缩zip包
    z = zipfile.ZipFile(cmdstr, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)   # 大文件压缩，默认FALSE
    for dirpath, dirnames, filenames in os.walk(strCVSPath):
        fpath = dirpath.replace(strCVSPath,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()

zip()
