import os
import datetime
import pandas as pd
import re



def check_time(Logdate, start, end):
    log_date = Logdate.split()

    st = datetime.date(int(start[2]), int(start[0]), int(start[1]))
    en = datetime.date(int(end[2]), int(end[0]), int(end[1]))
    lg = datetime.date(int(log_date[2]), int(log_date[0]), int(log_date[1]))

    if (st > lg):
        # log file date is before start-date
        return -1
    elif (en < lg):
        # log file date is after end-date
        return -1
    else:
        return 1


def validate_log(file, startDate, endDate):
    logPath = os.path.abspath(str(file))
    print("Log: %s" % logPath)
    dir = os.path.dirname(logPath)
    sd = startDate.split("/")
    ed = endDate.split("/")

    dir = dir.lower().endswith(('test_dir'))
    txt_Type = logPath.endswith('.txt')
    csvType = logPath.endswith('.csv')
    excelType = logPath.endswith('.xlsx')
    logType = logPath.endswith('.log')

    if (txt_Type or logType):
        print("in if")
        valid = txt_logs(file, sd, ed)
    elif (dir and csvType):
        print("csv and white dir")
        sd[1] = int(sd[1]) - 1
        ed[1] = int(ed[1]) + 1
        valid = csv_logs(file, sd, ed)

    elif (excelType):
        valid = excel_logs(file, sd, ed)

    elif (csvType):
        valid = csv_logs(file, sd, ed)
    else:
        valid = -1

    if (valid == 1):
        # proceed with splunk ingestion
        print("valid, proceed")
        return 1
    else:
        # enforcment action
        print("Timestamp out of bounds")
        return -1


def txt_logs(file, startDate, endDate):
    f = open(file, "r")
    content = f.read()
    pattern = "\d{2}[:]\d{2}\s\d{2}[/]\d{2}[/]\d{2}\s\w\w"
    dates = re.findall(pattern, content)
    for x in dates:
        p = x.split(" ")
        d = p[1].split("/")
        logDate = d[0] + " " + d[1] + " " + d[2]
        print("Timestamp: " + x)
        v = check_time(logDate, startDate, endDate)
        if (v == -1):
            return -1
    return v


def excel_logs(file, startDate, endDate):
    v = -1
    s = pd.read_excel(file).to_string()
    pattern = "\d{2}[:]\d{2}\s\d{2}[/]\d{2}[/]\d{2}\s\w\w"
    dates = re.findall(pattern, s)
    for x in dates:
        p = x.split(" ")
        d = p[1].split("/")
        logDate = d[0] + " " + d[1] + " " + d[2]
        print("Timestamp: " + x)
        v = check_time(logDate, startDate, endDate)
        if (v == -1):
            return -1
    return v


def csv_logs(file, startDate, endDate):
    v = -1
    s = pd.read_csv(file).to_string()
    pattern = "\d{2}[:]\d{2}\s\d{2}[/]\d{2}[/]\d{2}\s\w\w"
    dates = re.findall(pattern, s)
    for x in dates:
        p = x.split(" ")
        d = p[1].split("/")
        logDate = d[0] + " " + d[1] + " " + d[2]
        print("Timestamp: " + x)
        v = check_time(logDate, startDate, endDate)
        if (v == -1):
            return -1
    return v