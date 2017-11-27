import os
import time
source=["D:\\Algorithm Analysis & Design\\*.txt","D:\\Python source files\\*.py"]
print("source directory is:",source[0])
target_dir="G:\\backup"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today=target_dir+os.sep+time.strftime("%Y%m%d")
if not os.path.exists(today):
    os.mkdir(today)
now=time.strftime("%H%M%S")
target=today+os.sep+now
print("destination file name is:",target)

rar_command="rar a \"{0}\" \"{1}\"".format(target,"\" \"".join(source))
print("rar command is:",rar_command)
'''
if os.system(rar_command)==0:
   print("successful backup to",target)
else:
   print("backup failed")
os.system("ping baidu.com")
'''

