from excle_handle.get_excle_info import write_short_name,get_excel_request_data,write_reslut,write_result_to_xlsx
from Data_add_time import get_short_name
from File_upload import upload_file,get_file_date,get_file_name
import json
from Data_add_time import file_name_get,file_rename,file_path
def write_shortname_excel():
    """
    写shortname，fullname到表格中,已写，不用再执行了
    :return:
    """
    short_name = get_short_name("File_Order_Data", 15)
    full_file_name = file_name_get("File_Order_Data")
    write_short_name("../file/data.xlsx", full_file_name, 2)

def  request_send(row):
    """
    获取文件简称 →文件全称，路径 →修改文件名称，以防文件重复不支持上传
    获取请求数据 →根据修改的文件名称中获取文件时间 →将文件时间拼接到请求数据中
    :param row: Excel运行的行数，row是几，就运行几行
    :return:
    """
    for i in range(2,row+1):
        file_short_name,file_request_data = get_excel_request_data("../file/data.xlsx", i,3,8)
        full_file_name = get_file_name(file_short_name, "File_Order_Data")

        get_file_path =file_path(full_file_name)
        file_name = file_rename(get_file_path)

        date = get_file_date(file_name)
        file_time = json.dumps([{"name": file_name, "time": date}])
        file_request_data["file_times"] = file_time

        if file_request_data["process"] == None:
            continue
        response =upload_file(file_short_name, data=file_request_data)

        if response.json()['message']=="success":
            reslut="pass"
            write_reslut("../file/data.xlsx",reslut, i,7)
            write_result_to_xlsx("../file/data.xlsx",i,7, reslut)
        else:
            reslut ="fail"
            write_reslut("../file/data.xlsx", reslut, i, 7)
            write_result_to_xlsx("../file/data.xlsx", i, 7, reslut)


if __name__ == '__main__':
    # write_shortname_excel()
    request_send(28)