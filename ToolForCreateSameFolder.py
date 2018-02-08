# coding:utf-8
import os
import shutil

# currentpath = os.getcwd()
currentpath = "C:\\Users\\shenyu1.NUCTECH\\Desktop\\TIP"

# for file in os.listdir(currentpath):
#     filename = os.path.splitext(file)[0]
#     extension = os.path.splitext(file)[1]
#     filepath = os.path.join(currentpath, file)
#     if extension == '.img':
#         print(file)
#         newdirpath = os.path.join(currentpath, filename)
#         if not os.path.exists(newdirpath):
#             os.makedirs(newdirpath)
#             shutil.move(filepath, newdirpath)



def move_image(path):
    for file in os.listdir(path):
        filename = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        if os.path.isdir(os.path.join(path, file)):
            move_image(os.path.join(path, file))
        else:
            if extension == ".jpg":
                newdirpath = os.path.join(path, filename)
                if not os.path.exists(newdirpath):
                    os.makedirs(newdirpath)
                    shutil.move(os.path.join(path, file), newdirpath)


if __name__ == '__main__':
    move_image(currentpath)
