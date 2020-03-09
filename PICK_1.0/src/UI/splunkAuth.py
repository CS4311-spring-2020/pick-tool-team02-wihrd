import splunklib.client as client
import sys
from os import path
import os


HOST = 'localhost'
PORT = '8089'
USERNAME = 'wkoo05'
PASSWORD = 'splunkpw1'
def splunk_upload():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print(service)
    try:
        service.indexes.create("test_index")
    except:
        print("Index exits already")
    try:
        print("Uploading file")
        # Retrieve the index for the data
        myindex = service.indexes["test_index"]
        # Create a variable with the path and filename
        path = "C:\\Users\\wkoo0\\Videos\\test\\"
        # Upload and index the file
        # myindex.upload(path)

        directory = os.fsencode(path)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            concatString = path + filename
            print(concatString)
            myindex.upload(concatString)
            del concatString
            continue






    except Exception as e:
        print('error:')
        print(str(e))




if __name__ == '__main__':
    splunk_upload()