import splunklib.client as client
import sys
from os import path
import re
import os
import json
import splunklib.results as results
from LogValidation import validate_log
from Models import LogEntry
from Models.LogEntry import logEntry
from Models.LogFile import LogFile
from Models.EventConfiguration import EventConfiguration
from Models.EAR import EAR
#import numpy as np
import time

HOST = 'localhost'
PORT = '8089'
USERNAME = 'imhudson'
PASSWORD = 'Test1234'

def valTable():
    path = "C:\\Users\\wkoo0\\Videos\\test\\"
    directory = os.fsencode(path)
    validationList = []
    s = "03/20/2020"
    e = "04/26/2020"

    try:
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            concatString = path + filename
            log_date = time.ctime(os.path.getctime(concatString))
            print(concatString)
            val = validate_log(concatString, s, e)
            if(val == 1):
                obj = logEntry(" ", log_date, filename, concatString)
                print("Log ingested to splunk")
                validationList.append(obj)
                del concatString
            else:
                continue

    except Exception as e:
        print('error:')
        print(str(e))

    return validationList

def splunk_upload():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print(service)
    try:
        service.indexes.create("test_index8")
    except:
        print("Index exits already")
    try:
        print("Uploading file")
        # Retrieve the index for the data
        myindex = service.indexes["test_index8"]
        # Create a variable with the path and filename
        path = "C:\\Users\\wkoo0\\Videos\\test\\"
        # Upload and index the file
        # myindex.upload(path)

        directory = os.fsencode(path)

        #dates
        s = "03/20/2020"
        e = "04/26/2020"
        earList = []
        validationList = []

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            concatString = path + filename
            log_date = time.ctime(os.path.getctime(concatString))
            print(concatString)
            val = validate_log(concatString, s, e)
            if(val == 1):
                #print("Log ingested to splunk")
                myindex.upload(concatString)
                obj = LogEntry(" ", log_date, filename, concatString)
                validationList.append(obj)
                del concatString
            else:
                print("Here")
                obj = EAR(concatString, log_date, "", "", "Timestamp Out of Bounds")
                earList.append(obj)
                del concatString
            continue


    except Exception as e:
        print('error:')
        print(str(e))

    return earList


def splunkExport():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    rr = results.ResultsReader(service.jobs.export("search index=test_index8"))
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

            descResult = str(desc.values())
            #descResult.join(desc.values())
            sourceResult = str(source.values())
            # sourceResult.join(source.values())
            obj = logEntry(descResult, timestamp, name, sourceResult)

            # print(res)
            print(descResult)
            print(sourceResult)
            logEntryList.append(obj)

    #assert rr.is_preview == False

    return logEntryList


def importLogs():
     logList = list()
     eventconfig = EventConfiguration.getInstance()
     root = eventconfig.getRootDirectory()
     #root = "C:\\Users\\Dgarc\\Desktop\\test_dir"
     folders = ["Red", "Blue", "White"]
     for f in folders:
        dir = root + "\\" + f
        files = os.listdir(dir)
        for x in files:
            path = dir + "\\" + x
            timeStamp = time.ctime(os.path.getctime(path))
            log = LogFile(x, timeStamp, path, f)
            logList.append(log)
     return logList

if __name__ == '__main__':
    splunk_upload()
    #splunkExport()