import splunklib.client as client
import sys
from os import path
import re
import os
import splunklib.results as results
from LogValidation import validate_log

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

        #dates
        s = "02/26/2020"
        e = "03/26/2021"

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            concatString = path + filename
           #print(concatString)
            val = validate_log(concatString, s, e)
            if(val == 1):
                myindex.upload(concatString)
                del concatString
                continue
            else:
                continue

    except Exception as e:
        print('error:')
        print(str(e))

def splunkExport():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    rr = results.ResultsReader(service.jobs.export("search index=test_index"))
    substringSource = "source"
    substringDescription = "_raw"
    substringHost = "host"
    logEntryList = []

    for result in rr:
        if isinstance(result, results.Message):
            print("")
            # print('%s: %s' % (result.type, result.message))

        elif isinstance(result, dict):
            # Normal events are returned as dicts
            res = dict((k, result[k]) for k in [substringSource, substringHost, substringDescription] if k in result)
            logEntryList.append(res)

    assert rr.is_preview == False

    return logEntryList

if __name__ == '__main__':
    splunk_upload()
    splunkExport()