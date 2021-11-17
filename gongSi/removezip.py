import os, sys, time, zipfile,glob
###remove###
strZipPath = "D:" + os.sep + "mine"+  os.sep + "ddd" +  os.sep
for file in glob.glob(os.path.join(strZipPath,"*.zip")):
    os.remove(file)
