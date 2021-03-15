
import requests
import pytest

from config import file_upload_url,scm_url,login_scm
from file_handle import file_name_get,file_path
def test_scm_upload():
    header = {"cookie": "sessionid=w9r7a4f439o9ynj3z7f454en2s8x67z3",
              "accept": "application/json, text/plain, */*"}
    data_scm = {"process": 3,
                "supplier": 9,
                "file_type": 1}
    files = file_name_get("data")
    for file in files:
        if "WIP" in file:
            scm_file = file
    filepath = file_path(scm_file)
    upload_file = {'file': open(filepath, 'rb')}
    upload_json = requests.post(url=file_upload_url, data=data_scm, files=upload_file, headers=header)
    text= upload_json.text
    print(text)
if __name__ == '__main__':
    pytest.main(["-s","scm_test.py"])