import time
import  os,re,requests
import shutil
from config import file_base_url

#修改一个文件的名称
def file_rename(file_path):

    current_time = time.strftime("""%Y%m%d_%H%M%S""", time.localtime())
    file_url,file_name = os.path.split(file_path)
    index = file_name.rfind(".")

    new_file = "".join([file_name[:index-16],"_",current_time,file_name[index:]])
    new_file_path = os.path.join(file_url,new_file)
    os.rename(file_path,new_file_path)
    return new_file
#批量修改文件名称
def change_name(files):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))
    for file in files:
        print(file)
        file_path = os.path.join(current_path,"data",file)
        file_rename(file_path)


#复制文件夹
def copy_file(oldfile,newfile):
    if os.path.exists(oldfile):
        shutil.copyfile(oldfile,newfile)

#根据文件夹获取所有的文件名称
def file_name_get(folder_name):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))
    current_file_path = os.path.join(current_path,folder_name)
    #根据已有的路径，遍历文件夹
    file_list = os.listdir(current_file_path)
    return file_list

#根据文件简称获取单个文件名称
def get_file_name(file_short_name,folder_name):
    files = file_name_get(folder_name)
    for file in files:
        if file_short_name in file:
            scm_file = file
    return scm_file


def upload_file(file_name,folder,data):

    scm_file = get_file_name(file_name,folder)
    filepath = file_path(scm_file,folder)
    upload_file = {'file': open(filepath, 'rb')}
    file_upload_url = file_base_url + "wip/supplier-file/upload"

    response = requests.post(url=file_upload_url, data=data, files=upload_file)
    return response
#根据文件名称拼接文件路径
def file_path(file_name,folder_name):
    current_file = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.dirname(current_file))
    file_path_now = os.path.join(current_path,folder_name,file_name)
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
def get_file_date(file_name: str) -> str or None:
    """
    根据传入的文件名，获取文件的具体时间，返回值为日期格式，精确到日 2020-07-01

    Args:
        file_name (str): [description]

    Returns:
        str: [description]
    """
    file_name = file_name.replace('-', '').replace('_', ' ')
    reses = re.findall(r"\d{8}", file_name)
    dates = []
    for res in reses:
        year = res[:4]
        month = res[4:6]
        day = res[6:]
        file_date = '-'.join([year, month, day])
        dates.append(file_date)
    # 如果匹配到两个满足条件到日期，忽略
    if len(dates) == 0:
        return
    else:
        return dates[0]


if __name__ == '__main__':
    short_name = get_short_name("File_Order_Data",15)
    print(short_name)


    # filelist = file_name_get("data")
    # change_name(filelist)

    # copy_file(file_path("data"),file_path("newdata1"))
