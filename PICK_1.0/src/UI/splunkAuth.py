import splunklib.client as client
import sys
from os import path
import re
import os
import splunklib.results as results
from LogValidation import validate_log
from Models import LogEntry
from Models.LogEntry import logEntry

HOST = 'localhost'
PORT = '8089'
USERNAME = 'wkoo05'
PASSWORD = 'splunkpw1'

def splunk_upload():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print(service)
    try:
        service.indexes.create("test_index5")
    except:
        print("Index exits already")
    try:
        print("Uploading file")
        # Retrieve the index for the data
        myindex = service.indexes["test_index5"]
        # Create a variable with the path and filename
        path = "C:\\Users\\wkoo0\\Videos\\test\\"
        # Upload and index the file
        # myindex.upload(path)

        directory = os.fsencode(path)

        #dates
        s = "03/20/2020"
        e = "04/26/2020"

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            concatString = path + filename
           #print(concatString)
            val = validate_log(concatString, s, e)
            if(val == 1):
                #print("Log ingested to splunk")
                myindex.upload(concatString)
                del concatString
            continue

    except Exception as e:
        print('error:')
        print(str(e))

def splunkExport():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    rr = results.ResultsReader(service.jobs.export("search index=test_index5"))
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
            source = dict((k, result[k]) for k in [substringSource] if k in result)
            host = dict((k, result[k]) for k in [substringHost] if k in result)
            desc = dict((k, result[k]) for k in [substringDescription] if k in result)
            timestamp = ""
            name = ""

            obj = logEntry(desc.values(), timestamp, name, source.values())
            #print(res)
            print(desc.values())
            print(source.values())
            logEntryList.append(obj)

    assert rr.is_preview == False

    return logEntryList


if __name__ == '__main__':
    splunk_upload()
    #splunkExport()