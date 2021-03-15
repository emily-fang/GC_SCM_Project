import time
import  os
import shutil
#修改一个文件的名称
def file_rename(file_path):

    current_time = time.strftime("""%Y%m%d_%H%M%S""", time.localtime())
    file_url,file_name = os.path.split(file_path)
    index = file_name.rfind(".")
    # _index = file_name.rfind("_")
    new_file = "".join([file_name[:index-16],"_",current_time,file_name[index:]])
    # new_file = "".join([file_name[:_index],"_",current_time,file_name[index:]])
    new_file_path = os.path.join(file_url,new_file)
    os.rename(file_path,new_file_path)
    return new_file
#批量修改文件名称
def change_name(files):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))

    for file in files:
        print(file)
        file_path = os.path.join(current_path, "./File_Order_Data", file)
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
    file_path_now = os.path.join(current_path, "File_Order_Data", file_name)
    return file_path_now

def  get_short_name(folder_name,index):
    """
    :param folder_name: 根据传入的文件夹名称，获取所有的文件名称
    :param index: 文件名称截取前index位
    :return: 返回所有的根据参数index,截取的文件名称
    """
    file_list = file_name_get(folder_name)
    file_short_name = []
    for file in file_list:
        short_name =file[:index]
        file_short_name.append(short_name)
    return file_short_name


if __name__ == '__main__':
    filelist = file_name_get("File_Order_Data")
    change_name(filelist)

    # copy_file(file_path("data"),file_path("newdata1"))
