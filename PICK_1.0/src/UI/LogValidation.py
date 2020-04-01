import os
import time
import calendar


def check_time(Logdate, start, end):
    log_date = Logdate.split()
    m = list(calendar.month_abbr).index(log_date[1])
    if((int(start[0])> m) or ((int(start[0]) == m) and int(start[1] > log_date[2])) or (int(start[2] > log_date[4]))):
        #log file date is before start-date
        return -1
    elif((int(end[0])< m) or ((int(end[0]) == m) and int(end[1] < log_date[2])) or (int(end[2] < log_date[4]))):
        #log file date is after end-date
        return -1
    else:
        return 1

def validate_log(logPath, startDate , endDate):
    #logPath = os.path.abspath(str(file))
    print("Log: %s" % logPath)
    dir = os.path.dirname(logPath)
    log_date = time.ctime(os.path.getctime(logPath))
    print("Timestamp: %s" % log_date)
    sd = startDate.split("/")
    ed = endDate.split("/")

    dir = dir.lower().endswith(('white'))
    fileType = logPath.endswith('.csv')

    if(dir and fileType):
        print("csv and white dir")
        sd[1] = int(sd[1]) - 1
        ed[1] = int(ed[1]) - 1
        valid = check_time(log_date, sd, ed)
    else:
        valid = check_time(log_date, sd, ed)
    if(valid == 1):
        #proceed with splunk ingestion
        print("valid, proceed")
        return 1
    else:
        #enforcment action
        print("Timestamp out of bounds")
        return -1




"""
if __name__ == '__main__':
    s = "02/26/2020"
    e = "03/26/2021"
    file = "sample.txt"
    validate_log(file ,s, e)
"""