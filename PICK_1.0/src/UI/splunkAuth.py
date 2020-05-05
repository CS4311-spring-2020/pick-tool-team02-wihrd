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
from UI.Models.EAR import EAR
import time

HOST = 'localhost'
PORT = '8089'
USERNAME = 'admin'
PASSWORD = 'splunkpw1'

def valFoldCheck():
    path = "C:\\Users\\wkoo0\\Videos\\test\\"
    directory = os.fsencode(path)
    validationList = []
    s = "03/20/2020"
    e = "04/26/2020"

    try:
        print("I got here")
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
        print('error2:')
        print(str(e))

    return validationList

def splunk_upload():
    service = client.connect(host=HOST, port=PORT, username=USERNAME)
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
        s = str("03/20/2020")
        e = str("04/26/2020")
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
                obj = logEntry(" ", log_date, filename, concatString)
                validationList.append(obj)
                del concatString
            else:
                print("Here")
                obj = EAR(filename, log_date, "", "", "Timestamp Out of Bounds")
                earList.append(obj)
                del concatString
            continue


    except Exception as e:
        print('error1:')
        print(str(e))

    return earList


def splunkExport():
    service = client.connect(host=HOST, port=PORT, username=USERNAME)
    rr = results.ResultsReader(service.jobs.export("search index=test_index8"))
    substringSource = "source"
    substringDescription = "_raw"
    substringHost = "host"
    logEntryList = []
    i = 0

    for result in rr:
        if isinstance(result, results.Message):
            print("")
            # print('%s: %s' % (result.type, result.message))

        elif isinstance(result, dict):
            # Normal events are returned as dicts
            source = dict((k, result[k]) for k in [substringSource] if k in result)
            host = dict((k, result[k]) for k in [substringHost] if k in result)
            desc = dict((k, result[k]) for k in [substringDescription] if k in result)
            name = "Log " + str(i)

            i+=1
            descResult = str(desc.values()).split("dict_values(['",1)[1]
            timestamp = descResult[:24]
            descResult = descResult[24:]
            #descResult.join(desc.values())
            sourceResult = str(source.values()).split("dict_values(['",1)[1]
            # sourceResult.join(source.values())
            obj = logEntry(descResult, timestamp, name, sourceResult)

            # print(res)
            #print(descResult)
            #print(sourceResult)
            logEntryList.append(obj)

    #assert rr.is_preview == False
    print("TEEHEE")
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