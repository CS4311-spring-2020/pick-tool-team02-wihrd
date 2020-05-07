import pandas as pd
import re

def cleansing(path):
    #file = os.getfilename(path)
    txt_file_type = path.endswith('.txt')
    csv_file_type = path.endswith('.csv')
    excel_file_type = path.endswith('.xlsx')

    if (txt_file_type):
        showtxt(fileTXT)
        read_file(path)
    elif(csv_file_type):
        csv_file = rows(path)
        csv_file = colums(csv_file)
        clean_csv(csv_file)

    elif (excel_file_type):
        showcsv(fileEXCEL)
        excel_file = excel_rows(path)
        excel_file = excel_colums(excel_file)
        clean_excel(excel_file)
    else:
        print("error")

###############Text reader#####################
fileTXT = pd.read_csv(r'C:\Users\jesus\OneDrive\Desktop\data.txt', delimiter = '\t')
def showtxt(fileTXT):
    print("Before Cleansing a text file")
    fileTXT1 = pd.read_csv(r'C:\Users\jesus\OneDrive\Desktop\data.txt')
    print(fileTXT1)
    return fileTXT

def read_file(path):
    with open(path, 'r') as f:
      data = f.readlines()
    print("AFTER CLEANSING")
    p = " "
    for k in data:
     p = p + re.sub(r"[^a-zA-Z0-9]+", ' ', k) + '\n'
    print(p)

    text_file = open("OutputTxt.txt", "w")
    text_file.write(p)
    text_file.close()

################CSV reader#####################

def rows(csvPATH):
    csvPATH = pd.read_csv(csvPATH)
    filtered_data = csvPATH.dropna(axis='rows', how='all')
    return filtered_data

def colums(csvPATH1):
    csvPATH2 = csvPATH1.dropna(axis='columns', how='all')
    return csvPATH2

def clean_csv(csvPATH2):
    print("After Cleansing a CSV file ")
    cleansedCSV = colums(csvPATH2).to_string()
    print(cleansedCSV)

    text_file = open("OutputCSV.txt", "w")
    text_file.write(cleansedCSV)
    text_file.close()

##############Excel reader#####################
fileEXCEL = pd.read_excel(r'C:\Users\jesus\OneDrive\Desktop\data.xlsx')
def showcsv(fileEXCEL):
    print("Before Cleansing a Excel file")
    fileEXCEL1 = pd.read_excel(r'C:\Users\jesus\OneDrive\Desktop\data.xlsx')
    print(fileEXCEL1)
    return fileEXCEL

def excel_rows(excelPATH):
    excelPATH = pd.read_excel(excelPATH)
    filtered_data = excelPATH.dropna(axis='rows', how='all')
    return filtered_data


def excel_colums(excelPATH1):
    excelPATH2 = excelPATH1.dropna(axis='columns', how='all')
    return excelPATH2

def clean_excel(excelPATH2):
    print("After Cleansing a Excel file ")
    cleansedExcel = excel_colums(excelPATH2).to_string()
    print(cleansedExcel)

    text_file = open("OutputExcel.txt", "w")
    text_file.write(cleansedExcel)
    text_file.close()


if __name__ == '__main__':
    file_path = 'C:\\Users\\jesus\\OneDrive\\Desktop\\data.txt'
    cleansing(file_path)







