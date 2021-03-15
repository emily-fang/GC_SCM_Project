#-*- coding:utf-8 -*-
import requests
from excle_handle.get_excle_info import get_excel_request_data
from config import scm_base_url
import json,jsonpath
class ShipTO():
    """
    ship to 操作，选择lot操作，手动输入操作，int方法中全局变量的赋值后期可以封装起来，kwargs[key] = getattr(self,key)
    """
    def __init__(self,data):
        login_data = {"name": "emily_fang@wochacha.com", "password": "admin123"}
        login_url = scm_base_url+"users/user/login/"
        self.session = requests.session()
        self.session.post(login_url, data=login_data)
        self.data = data
        self.wip_ids = None
        self.wafer_qty = None
        self.data_id =None

    def  ship_banlance(self):
        scm_url = scm_base_url+"dispatch/ship-balance?"
        response_scm = self.session.get(scm_url, params=self.data)
        text = response_scm.text
        scm_json = json.loads(text)
        global flow_now_id
        flow_now_id = scm_json['data']['list'][0]["flow_node_id"]


    def ship_main(self):
        # ship_main操作，获取 ship_main_id,用于 ship_lot
        ship_main_url = scm_base_url+"dispatch/ship-main/"
        requests_data = {"params": self.data}
        response_scm = self.session.post(ship_main_url, json=requests_data)
        text = response_scm.text
        ship_json = json.loads(text)
        global ship_info_id,ship_main_id
        ship_info_id = ship_json['data']['ship_mains'][0]['ship_infos'][0]["id"]
        ship_main_id = ship_json['data']['ship_mains'][0]["id"]


    def ship_lot(self):
        ship_lot_url = scm_base_url+"dispatch/ship-lot?/"
        # ship_lot_url = "https://gc-scm-alpha.wochacha.cn/api/dispatch/ship-lot?/"
        ship_data = {"lot_type":self.data["lot_type[]"], "ship_main_id": ship_main_id, "flow_node_id": flow_now_id}
        response_scm = self.session.get(ship_lot_url, params=ship_data)
        text = response_scm.text
        scm_json = json.loads(text)

        wip_ids = scm_json['data']['list'][0]["wip_ids"]
        wafer_qty = scm_json['data']['list'][0]["wafer_qty"]
        if wip_ids:
            self.wip_ids = wip_ids
        if wafer_qty:
            self.wafer_qty = wafer_qty
        return wafer_qty

    def assign_by_lots(self):
        assign_by_lots_url = scm_base_url+f"dispatch/ship/{ship_info_id}/assign-by-lots"

        self.wip_data = json.dumps({"wip_ids": self.wip_ids, "lot_type": self.data["lot_type[]"]})
        self.header = {"content-type": "application/json;charset=UTF-8", "accept": "application/json, text/plain, */*"}
        self.session.patch(url=assign_by_lots_url, data=self.wip_data, headers=self.header)

    def input_lots(self,amount):
        amount_url = scm_base_url+f"dispatch/ship/{ship_info_id}"
        self.session.put(amount_url, data={"assigned_mp_qty": amount})


    def email(self):

        email_url = scm_base_url+"dispatch/email/"
        email_data = json.dumps([{"object_id": ship_main_id, "content_type": "shipmain"}])
        header = {"content-type": "application/json;charset=UTF-8"}
        response_scm = self.session.post(email_url, data=email_data, headers=header)
        text = response_scm.text
        email_json = json.loads(text)
        data_id = email_json['data'][0]['id']
        if data_id:
            self.data_id = data_id

    def update_sender(self):

        sender_url = scm_base_url+f"dispatch/email/{self.data_id}/"
        sender_data = {"receiver": ["emily_fang@wochacha.com"], "cc": ["emily_fang@wochacha.com"]}
        self.session.patch(sender_url, data=sender_data)

    def send_email(self):

        send_url = scm_base_url+"dispatch/email/send"
        ids = {"ids": self.data_id}
        self.session.post(send_url, data=ids)


if __name__ == '__main__':
    test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 2, 2, 7)

    # ship_to = ShipTO(reqest_data)
    # ship_to.ship_banlance()
    # ship_to.ship_main()
    #
    # ship_to.input_lots(1)
    # ship_to.email()
    # ship_to.update_sender()
    # ship_to.send_email()

    ship_to = ShipTO(reqest_data)
    ship_to.ship_banlance()
    ship_to.ship_main()

    print(ship_to.ship_lot())
    # ship_to.assign_by_lots()

    # ship_to.email()
    # ship_to.update_sender()
    # ship_to.send_email()


