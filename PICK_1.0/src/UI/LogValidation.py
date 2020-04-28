import os
import time
import datetime
import calendar
from Models.EAR import EAR


def check_time(Logdate, start, end):
    log_date = Logdate.split()
    m = list(calendar.month_abbr).index(log_date[1])

    sd = datetime.date(int(start[2]), int(start[0]), int(start[1]))
    ed = datetime.date(int(end[2]), int(end[0]), int(end[1]))
    lg = datetime.date(int(log_date[4]), int(m), int(log_date[2]))

    if(sd>lg):
        #log file date is before start-date
        return -1
    elif(ed<lg):
        #log file date is after end-date
        return -1
    else:
        return 1

def validate_log(file, startDate , endDate):
    earList = []
    logPath = os.path.abspath(str(file))
    print("Log: %s" % logPath)
    dir = os.path.dirname(logPath)
    log_date = time.ctime(os.path.getctime(logPath))
    print(log_date)
    sd = startDate.split("/")
    ed = endDate.split("/")

    dir = dir.lower().endswith(('white'))
    fileType = logPath.endswith('.csv')

    if(dir and fileType):
        print("csv and white dir")
        sd[1] = int(sd[1]) - 1
        ed[1] = int(ed[1]) + 1
        valid = check_time(log_date, sd, ed)
    else:
        valid = check_time(log_date, sd, ed)
    if(valid == 1):
        #proceed with splunk ingestion
        print("valid, proceed")
        return 1
    else:
        #enforcment action
        obj = EAR(logPath, log_date, "", "", "Timestamp out of bounds")
        earList.append(obj)
        print("Timestamp out of bounds")
        return -1





"""
if __name__ == '__main__':
    s = "02/26/2020"
    e = "03/26/2021"
    file = "sample.txt"
    validate_log(file ,s, e)
"""