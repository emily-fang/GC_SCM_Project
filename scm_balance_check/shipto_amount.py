import requests
import json
from file_handle import file_path,get_file_name
from config import scm_base_url,file_upload_url

from excle_handle.get_excle_info import get_excel_request_data
from Ship_TO import  ShipTO
#在GC_SCM系统中根据相应的参数获取可ship to的余量
def  balance_amount(request_data):
    login_data = {"name": "emily_fang@wochacha.com", "password": "admin123"}
    login_url = scm_base_url+"users/user/login/"
    session = requests.session()
    session.post(login_url, data=login_data)

    # GC_SCM查看ship-balance
    scm_url =scm_base_url+ "dispatch/ship-balance?"
    response_scm = session.get(scm_url,params=request_data)
    json_data =response_scm.json()['data']['list'][0]["inv_quantity"]
    print(json_data)
    return json_data

def shipto_bylot(row):
    '''
    :param row: row首行参数名称和第几行（row）的参数值拼接
    :param col: col是从第几列开始参数拼接
    :return:
    '''

    test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", row, 2, 7)

    ship_to = ShipTO(reqest_data)
    ship_to.ship_banlance()
    ship_to.ship_main()
    lot_amount = ship_to.ship_lot()
    ship_to.assign_by_lots()
    ship_to.email()
    ship_to.update_sender()
    ship_to.send_email()

    return lot_amount

def shipto_byamount(row,input_amount):
    test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", row, 2, 7)

    ship_to = ShipTO(reqest_data)
    ship_to.ship_banlance()
    ship_to.ship_main()

    ship_to.input_lots(input_amount)
    ship_to.email()
    ship_to.update_sender()
    ship_to.send_email()
    return  input_amount

def upload_file(file_name,data):
    scm_file = get_file_name(file_name,"data")
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    response = requests.post(url=file_upload_url, data=data, files=upload_file)
    return response
if __name__ == '__main__':
    test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 2, 2, 7)
    print(reqest_data)
    balance_amount(reqest_data)
