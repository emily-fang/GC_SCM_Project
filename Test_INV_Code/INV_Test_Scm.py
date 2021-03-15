#-*- coding:utf-8 -*-
import requests
import pytest
import json
from INV_shipto_amount import amount,wip_upload,GC_pl_upload,upload
from config import file_upload_url,scm_url,login_scm
from INV_Data_add_time import file_name_get,file_path,change_name

# class TestScm:
@pytest.fixture(name="login", scope='function')
def login_scm():
    login_data = {"name": "emily_fang@wochacha.com", "password": "admin123"}
    login_url = "https://gc-scm-alpha.wochacha.cn/api/users/user/login/"
    requests.post(login_url, data=login_data)
    print("登录成功")
    yield
    filelist = file_name_get("Test_INV_data")
    change_name(filelist)

#上传文件，检查数量是否正确
# def test_wip_upload(login):
# #上传HL/Visera的wip文件,数据重复
# #1、lot ID重复又是INV的数据已测试，会判断两行为错误
#     # HL_wip_response = wip_upload("HL_WIP_INV","3","9","1")
#
#     visera_wip_bank_response =wip_upload("visera_WIP__bank","22","4","1")
#     visera_wip_wafer_response =wip_upload("visera_WIP_no_waferid","22","4","1")
#     visera_wip_flow_response =wip_upload("VisEra_WIP_noflow","22","4","1")
#     visera_wip_response =wip_upload("VISEra_WIP_BANK","22","4","1")
#
#     assert visera_wip_response.status_code == 200
#     assert visera_wip_bank_response.status_code == 200
#     assert visera_wip_flow_response.status_code == 200
#     assert visera_wip_wafer_response.status_code == 200

def test_upload(login):
    # data={"process":"3","supplier":"9","file_type":"1"}
    HL_test_response = upload("HL_WIP_INV",process=3,supplier=9,file_type=1)
    print(HL_test_response.json())

    # assert HL_wip_response.status_code == 200
#


# def test_GC_pl_upload(login):
#     #GC供应商字段为空判断错误，wip关联失败也判断错误
#     # response = GC_pl_upload("Galaxycore_WH_IN_ZJ","77","171","2","1")
#
#     #GC_out文件的上传
#     OUT_Reponse=GC_pl_upload("Galaxycore_CP_OUT","77","171","2","2")
#     assert OUT_Reponse.status_code == 200
#     # assert response.status_code == 200

if __name__ == '__main__':
    pytest.main(["-s","INV_Test_Scm.py"])
