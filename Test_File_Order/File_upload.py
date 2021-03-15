import requests
import json
import re
from  config import scm_url
from  Data_add_time import file_name_get,file_path,change_name
from config import file_upload_url,scm_url

#在GC_SCM系统中根据相应的参数获取可ship to的余量
def  amount(request_data):

    header={"accept": "application/json, text/plain, */*",
            "cookie":"csrftoken=tNHw2T7KDQU1fTBIeIKejwwSXzwoGAINmOx9SbtSFoQjhAUSXY52FkzzqFdi6sJt; "
                     "sessionid=p4oogfy1edqw5u0pywsq77yij7i0zkyx",
            "referer": "https: // gc - scm - alpha.wochacha.cn / production - index / shipTo",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" }

    response_scm = requests.get(scm_url,params=request_data,headers=header)
    text=response_scm.text
    scm_json = json.loads(text)
    json_data =scm_json['data']['list'][0]["inv_quantity"]
    print(json_data)
    print(response_scm.json().keys())
    return json_data
#上传wip 文件
def wip_upload(file_name,process,supplier,file_type):
#普通供应商的wip/pl文件上传
    data_scm = {"process": process,
                "supplier": supplier,
                "file_type": file_type}
    files = file_name_get("File_Order_Data")
    for file in files:
        if file_name in file:
            scm_file = file
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    response = requests.post(url=file_upload_url, data=data_scm, files=upload_file)
    return response
#格科供应商中转供应商的 in/out文件上传
#上传PL文件
def  GC_pl_upload(file_name,process,supplier,file_type,pl_type):
    data_scm = {"process": process,
                "supplier": supplier,
                "file_type": file_type,
                "pl_type":pl_type}
    files = file_name_get("File_Order_Data")
    for file in files:
        if file_name in file:
            scm_file = file
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    response = requests.post(url=file_upload_url, data=data_scm)
    return response
#根据文件名称的缩写，获取文件全称
def get_file_name(file_short_name,folder_name):
    files = file_name_get(folder_name)
    for file in files:
        if file_short_name in file:
            scm_file = file
    return scm_file

def upload_file(file_name,data):

    scm_file = get_file_name(file_name,"File_Order_Data")
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}

    response = requests.post(url=file_upload_url, data=data, files=upload_file)
    return response

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