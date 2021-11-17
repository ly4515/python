import os, sys, time, zipfile,shutil,glob
strCVSPath = "D:/mine/test"  #要压缩的文件夹路径
strZipPath = "D:" + os.sep + "mine"+  os.sep + "ddd" +  os.sep # 压缩后存放路径
new_path = "D:" + os.sep + "mine" +  os.sep
timelist = time.localtime()
year = str(timelist[0])
month = str(timelist[1])
day = str(timelist[2])
strFileName = year + "_" + month + "_" + day +'.zip' # 压缩包名
cmdstr = strZipPath + strFileName
z = zipfile.ZipFile(cmdstr,'w',zipfile.ZIP_DEFLATED,allowZip64=True)
for dirpath, dirnames, filenames in os.walk(strCVSPath):
    fpath = dirpath.replace(strCVSPath,'')
    fpath = fpath and fpath + os.sep or ''
    for filename in filenames:
        z.write(os.path.join(dirpath, filename),fpath+filename)
z.close()
pa = os.getcwd() #获取当前工作目录路径
print(pa)
cmd = "del " + strZipPath + "*.* /Q"
os.system(cmd)