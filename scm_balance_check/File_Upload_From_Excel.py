from  excle_handle.get_excle_info import write_short_name,get_excel_request_data

from file_handle import get_short_name,get_file_name,file_path,file_rename,get_file_date,upload_file,file_name_get
import json
def write_shortname_excel():
    """
    写shortname，fullname到表格中,已写，不用再执行了
    :return:
    """
    short_name = get_short_name("scm_data", 15)
    full_file_name = file_name_get("scm_data")
    write_short_name("./scm_data/request_data.xlsx", full_file_name, 1)
    write_short_name("./scm_data/request_data.xlsx", short_name, 2)

def file_upload(folder,file_short_name):
    full_files_name = file_name_get(folder)

    full_file_name = get_file_name(file_short_name,folder)
    get_file_path = file_path(full_file_name,folder)
    file_name = file_rename(get_file_path)

    for file in full_files_name:
        if file_short_name in  file:
            date = get_file_date(file_name)
            file_time = json.dumps([{"name": file_name, "time": date}])
            file_request_data ={"process":3,"supplier":9}
            file_request_data["file_times"] = file_time
            if "WIP" in file_short_name:
                file_request_data["file_type"]= 1
            if "PL"  in  file_short_name:
                file_request_data["file_type"]= 2
            response = upload_file(file_short_name,folder,data=file_request_data)
            print(response.json())


if __name__ == '__main__':
    file_upload("scm_data", "011_HL_WIP_202")
    # file_upload("scm_data", "2_PL_HL_CP_qty_201")
    # file_upload("scm_data", "7_PL_HL_CP_qty_200_")