import requests
import json
from  config import scm_url
from  INV_Data_add_time import file_name_get,file_path,change_name
from config import file_upload_url,scm_url,login_scm

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
    files = file_name_get("Test_INV_data")
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
    files = file_name_get("Test_INV_data")
    for file in files:
        if file_name in file:
            scm_file = file
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    response = requests.post(url=file_upload_url, data=data_scm, files=upload_file)
    return response
def upload(file_name,**data):

    files = file_name_get("Test_INV_data")
    for file in files:
        if file_name in file:
            scm_file = file
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    response = requests.post(url=file_upload_url, data=data, files=upload_file)
    return response