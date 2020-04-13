import os
ori_path = 'I:/dish_image/cv_image_ros5'
new_path = 'I:/dish_image/images'
j = 0
k = 772
for i in os.listdir(ori_path):
    if j%33==0:
        oldname = ori_path + os.sep + i  # os.sep添加系统分隔符
        newnum = str(k).zfill(6)
        # 设置新文件名0
        newname = new_path + os.sep + newnum + '.jpg'
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)
        k += 1
    j += 1

