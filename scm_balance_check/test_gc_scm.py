#-*- coding:utf-8 -*-
from database_operate import DataBase
import requests,pytest
import time
from shipto_amount import balance_amount,shipto_bylot,shipto_byamount
from File_Upload_From_Excel import file_upload
from excle_handle.get_excle_info import get_excel_request_data
class TestScm(object):
    def setup_class(self):
        '''
        测试之前先清除所测试的数据，然后再导入所测试数据的wip文件
        '''
        sql = "DELETE  FROM wip.wip_data WHERE  raw_version in('ADBB','EOEB','KOGB','EODB','IAQB','KOHB')"
        DataBase().select_update(sql)
        time.sleep(2)
        file_upload("scm_data", "011_HL_WIP_202")
        time.sleep(5)
    def teardown_class(self):
        DataBase().database_close()

    @pytest.mark.smoke
    def test_one(self):
        '''
        250→220,EOEB
        1、入库PL数量小于 ship to 数量
        2、PL 入库部分lot相同，部分不同
        '''
        test_num,reqest_data =get_excel_request_data("../scm_data/scm_request_data.xlsx", 2, 2, 7)
        ship_before = balance_amount(reqest_data)
        ship_lot = shipto_bylot(2)
        ship_after = ship_before - ship_lot
        time.sleep(5)

        file_upload("scm_data", "1_PL_HL_CP_qty_30_ship10")
        time.sleep(5)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_after-5)

    def test_two(self):
        '''
        balance201，指定lot25个做ship to,入PL(lot与已ship to相同15个，不同10个，4个原先非INV的数据)
        1、入库pl数量大于ship to 数量，KOGB,201→166
        2、PL入库部分与已ship 相同，部分与已ship 不同
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 3, 2, 7)
        ship_before = balance_amount(reqest_data)
        ship_lot = shipto_bylot(3)
        ship_after = ship_before - ship_lot
        time.sleep(3)
        file_upload("scm_data", "2_PL_HL_CP_qty_201")
        time.sleep(3)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_after-10)

    def test_three(self):
        '''
        381→336
        EODB 381个，ship to 30(指定25，数量5)，入PL文件40个（已ship20个，INV20个）
        1、入库pl数量大于ship to 数量：分别为指定lot和按数量分配
        2、PL入库部分与该行数据已有的相同
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 4, 2, 7)
        ship_before = balance_amount(reqest_data)
        ship_lot = shipto_bylot(4)
        entry_lot = shipto_byamount(4,5)
        time.sleep(3)
        ship_after = ship_before - ship_lot-entry_lot
        # 入PL文件36个，已shipped25个， 未ship to11个
        file_upload("scm_data", "3_PL_HL_CP_qty")
        time.sleep(3)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_after-15)


    def  test_four(self):
        '''
        EODB  336→306,这个可能还要再确定？
        入库pl文件的指定与ship to 指定lotID一致
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 5, 2, 7)
        ship_before = balance_amount(reqest_data)
        ship_lot = shipto_bylot(5)
        ship_after = ship_before - ship_lot
        # 入PL文件25个，已shipped25个的lot一样
        time.sleep(4)
        file_upload("scm_data", "4_PL_HL_CP")
        time.sleep(4)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == ship_after

    def test_five(self):
        '''
        入库48个，按数量做了10个，balance为 38，入PL5个后，balance为43，这种情况好像是对的，能走通
         按数量ship to，入库PL数量小于 ship to 数量
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 6, 2, 7)
        ship_before = balance_amount(reqest_data)
        entry_lot = shipto_byamount(6,10)
        time.sleep(4)
        file_upload("scm_data", "5_PL_HL_CP_qty_48")
        time.sleep(4)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_before - 5)

    # @pytest.mark.smoke
    def test_six(self):
        '''
        KOHB 101，按数量11个ship to,入库15个,101→86
        1、入库PL数量大于 ship to数量
        2、入库PL的lotID部分与该行数据已有的相同，部分不相同
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 7, 2, 7)
        ship_before = balance_amount(reqest_data)
        shipto_byamount(7,11)
        time.sleep(4)
        file_upload("scm_data", "6_PL_HL_CP_qty")
        time.sleep(3)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_before-15)

    def test_seven(self):
        '''92→77
        ADBB 92,数量12个做ship to,入库PL15个
        1、入库PL的lot ID大于 ship to 数量
        2、入库pl的lot id 与该行数据已有的lotID相同
        '''
        test_num, reqest_data = get_excel_request_data("../scm_data/scm_request_data.xlsx", 8, 2, 7)
        ship_before = balance_amount(reqest_data)
        shipto_byamount(8,12)
        # 入库PL数据15个
        time.sleep(3)
        file_upload("scm_data", "7_PL_HL_CP_qty_200_")
        time.sleep(4)
        balance_QTY = balance_amount(reqest_data)
        assert balance_QTY == (ship_before -15)

if __name__ == '__main__':
    pytest.main(["-s","-v","test_gc_scm.py","-m smoke"])
