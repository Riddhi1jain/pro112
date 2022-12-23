import os
import shutil
from_dir="C:/Users/Jain/Downloads"
to_dir="C:/Users/Jain/Documents/whitehat/projects/pro111"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for filename in list_of_files:
    name,extension=os.path.splitext(filename)


    if(extension==''):
      continue
    if extension in['.txt','.doc','.docx','pdf']:
        path1=from_dir + '/' + filename
        path2=to_dir + '/' + "Image_Files"
        path3=to_dir + '/' + "Image_Files" + '/' + filename
 
        if os.path.exists(path2):
         print("Moving" + filename + ".....")
         shutil.move(path1,path3)

        else:
         os.makedirs(path2)
         print("Moving" + filename + ".....")
         shutil.move(path1,path3)