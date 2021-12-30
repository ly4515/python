import os
strZipPath = "D:" + os.sep + "mine"+  os.sep + "ddd" +  os.sep
cmd = "del " + strZipPath + "*.* /Q"
os.system(cmd)
