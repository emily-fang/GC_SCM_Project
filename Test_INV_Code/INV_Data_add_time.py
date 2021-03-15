import time
import  os
import shutil
#修改一个文件的名称
def file_rename(file_path):

    current_time = time.strftime("""%Y%m%d_%H%M%S""", time.localtime())
    file_url,file_name = os.path.split(file_path)
    index = file_name.rfind(".")

    new_file = "".join([file_name[:index-16],"_",current_time,file_name[index:]])
    new_file_path = os.path.join(file_url,new_file)
    os.rename(file_path,new_file_path)
#批量修改文件名称
def change_name(files):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))

    for file in files:
        print(file)
        file_path = os.path.join(current_path, "./Test_INV_data", file)
        file_rename(file_path)


#复制文件夹
def copy_file(oldfile,newfile):
    if os.path.exists(oldfile):
        shutil.copyfile(oldfile,newfile)

#获取文件名称
def file_name_get(folder_name):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))
    current_file_path = os.path.join(current_path,folder_name)
    #根据已有的路径，遍历文件夹
    file_list = os.listdir(current_file_path)
    return file_list

#根据文件名称拼接文件路径
def file_path(file_name):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))
    file_path_now = os.path.join(current_path, "./Test_INV_data", file_name)
    return file_path_now

if __name__ == '__main__':
    filelist = file_name_get("Test_INV_data")
    change_name(filelist)

    # copy_file(file_path("data"),file_path("newdata1"))
