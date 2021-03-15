#-*- coding:utf-8 -*-

from INV_shipto_amount import upload
from INV_Data_add_time import file_name_get,change_name

filelist = file_name_get("Test_INV_data")
change_name(filelist)

def test_upload():
# 上传VISEra的wip 文件
    upload("VISEra_WIP_BANK", process=22, supplier=4, file_type=1)
    upload("visera_WIP_no_flow", process=22, supplier=4, file_type=1)
    upload("visera_WIP_no_waferid", process=22, supplier=4, file_type=1)


#上传HL的wip文件
    upload("HL_WIP_INV",process=3,supplier=9,file_type=1)

#上传格科仓库的IN/out文件
    upload("Galaxycore_WH_IN_ZJ_nom",process=77,supplier=171,file_type=2,pl_type=1)
    upload("Galaxycore_CP_OUT", process=77, supplier=171, file_type=2, pl_type=2)
# 上传 smic 的wip 文件
    upload("SMIC_wip_version",process=1,supplier=3,file_type=1)
# 上传WLCSP的wip 文件
    upload("WIP_WLCSP", process=27, supplier=6, file_type=1)


if __name__ == '__main__':
    test_upload()
