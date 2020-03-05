import splunklib.client as client
import sys
from os import path


HOST = 'localhost'
PORT = '8089'
USERNAME = 'digarci13'
PASSWORD = 'blackvenom13'
def splunk_upload():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print(service)
    try:
        service.indexes.create("test_index")
    except:
        print("Index exits already")
    try:
        # Retrieve the index for the data
        myindex = service.indexes["test_index"]
        # Create a variable with the path and filename
        path = "C:\\Users\\Dgarc\\Desktop\\Software2\\Splunk\\root_dir\\Log2.txt"
        # Upload and index the file
        myindex.upload(path)




    except Exception as e:
        print('error:')
        print(str(e))




if __name__ == '__main__':
    splunk_upload()