#-*- coding:utf-8 -*-

from File_upload import upload_file,get_file_date,get_file_name
import json
from Data_add_time import file_name_get,change_name,file_rename,file_path
# #批量修改文件的名称
# filelist = file_name_get("File_Order_Data")
# change_name(filelist)

def test_upload():
# 上传VISEra的wip 文件
#     file_short_name="21_VISEra_WIP"
#     file_short_name="99_Galaxycore_WH_IN_2021"
#     file_short_name="8_PL_VISERA_OCF"
    # file_short_name="121_Galaxycore_CP"
    # file_short_name="100_Galaxycore_WH"
    # file_short_name ="PL_VISERA_20210"
    # file_short_name ="33_PL_HL_C_"
    try:
        # file_short_name ="01_HL_WIP_quancuo"
        # file_short_name = "CanSemi_WIP_report_release"
        # file_short_name = "GC5035-3_PL_WLCSP_CSP"
        file_short_name ="V_VISEra_WIP_2021"
        full_file_name = get_file_name(file_short_name, "File_Order_Data")
    except Exception as e:
        print(e)
    get_file_path =file_path(full_file_name)
    file_name = file_rename(get_file_path)

    date = get_file_date(file_name)
    file_time = json.dumps([{"name": file_name, "time": date}])
    response =upload_file(file_short_name, process=22, supplier=4, file_type=1,file_times=file_time)

    print(response.json())
    #
    # file_short_name ="8_PL_VISERA_OCF"
    # upload_file(file_short_name, process=22, supplier=4, file_type=2,file_times=file_time)




 #GCSH的仓库入库IN文件
    # upload(file_short_name, process=77,supplier=170,file_type=2,pl_type=2,file_times=file_time)

#格科仓库cp制程 GCZJ入WIP文件
# Alpha 环境   upload(file_short_name, process=77, supplier=165, file_type=1, file_times=file_time)
#beta环境  upload(file_short_name, process=3, supplier=11, file_type=1, file_times=file_time)

#VISERA制程下wip 文件
# upload(file_short_name, process=22, supplier=4, file_type=1,file_times=file_time)
# upload_file(file_short_name, process=22, supplier=4, file_type=2,file_times=file_time)
#

# #上传HL的wip文件，process=3,supplier=9
# upload_file(file_short_name, process=3, supplier=9, file_type=2, file_times=file_time)
# upload_file(file_short_name, process=3, supplier=9, file_type=1, file_times=file_time)

#alpha GCZJ入库的IN/out文件，beta环境GCZJ的supplie是172
    #  upload_file(file_short_name, process=77, supplier=171, file_type=2, pl_type=1,file_times=file_time)
    # upload_file(file_short_name, process=77, supplier=171, file_type=2, pl_type=2,file_times=file_time)

# 上传 smic 的wip 文件，process=1，supplier=3
#     upload("SMIC_wip_version",process=1,supplier=3,file_type=1)

# #上传WLCSP的wip 文件，process=27, supplier=6
#     upload_file("WIP_WLCSP", process=27, supplier=6, file_type=1)

#上传Cansemi的wip 文件，process =1,supplier=13
# upload_file(file_short_name, process=1, supplier=13, file_type=1, file_times=file_time)


if __name__ == '__main__':
    test_upload()
