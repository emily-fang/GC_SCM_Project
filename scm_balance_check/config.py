import pytest
import requests

'''
如果要把环境切换成beta，数据库配置还得再改一下
'''
file_base_url = "https://gc-scm-file-alpha.wochacha.cn/api/"
file_upload_url = file_base_url+"wip/supplier-file/upload"
scm_base_url ="https://gc-scm-alpha.wochacha.cn/api/"
#GC_SCM查看ship-balance
# scm_url = "https://gc-scm-alpha.wochacha.cn/api/dispatch/ship-balance?"

@pytest.fixture(name="login",scope='function')
def login_scm(request):
    login_data = {"name": "emily_fang@wochacha.com", "password": "admin123"}
    login_url = "https://gc-scm-alpha.wochacha.cn/api/users/user/login/"
    response=requests.post(login_url, data=login_data)
    print(response.json())
