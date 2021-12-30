import os, sys, time, zipfile
strCVSPath = "D:/mine/test"  #要压缩的文件夹路径
strZipPath = "D:" + os.sep + "mine"+  os.sep + "ddd" +  os.sep
new_path = "D:" + os.sep + "mine" +  os.sep
timelist = time.localtime()
year = str(timelist[0])
month = str(timelist[1])
day = str(timelist[2])
strFileName = year + "_" + month + "_" + day +'.zip'
cmdstr = strZipPath + strFileName # 压缩后文件夹的名字
z = zipfile.ZipFile(cmdstr,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
