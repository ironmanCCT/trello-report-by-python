##1.export your file to xlsx format with 2 coloumns, [casename, attachments] using TrelloExport Google Chrome Add-on. 
##2.place this script and xlsx export file into same folder
##3. requires python 3.7+ and the imported packages.
##4. you can adjust the sleep timer to be shorter than the default 5 seconds to download files faster.

import os
import requests
from openpyxl import load_workbook
import re
import pprint
import time
workbook = load_workbook(filename='YOUR_XLSX_FILE_NAME.xlsx')
worksheet = workbook['TrelloExport']
#attachments = []
#caseNames=[]

cwd = os.getcwd()  ##find the current working directory
print('current working directory: ' + cwd)



    #556 cards
for i in range(1,557):
    print('loop number:' + str(i))
    if(not worksheet.cell(i,2).value):
        print(str(i)+' has no attachments')
    else:
        #print('worksheet.cell('+str(i)+').value: ')
        #print(worksheet.cell(i,2).value)
        attachment = (worksheet.cell(i,2).value)
        results = []
        results.append(re.findall('(\[.*\]) (\(.*\)) (https.*)$', attachment, flags= re.MULTILINE))
        #print('results: ' + str(results))
        caseName = worksheet.cell(i,1).value
        caseName = caseName.replace('/', '-')
        print('caseName: ' + caseName)
        #caseNames.append(worksheet.cell(i,1).value)
        path = cwd + '\\' + caseName
        print('path exists? ' + str(os.path.isdir(path)))
        print("%s is the staged path" % path)
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s " % path)
        else:
            print ("%s directory probably exisits " % caseName)
            continue
        #download the attachments and save them to the caseName Directory
        for result in results:
            #print(result)
            try:
                for name_and_id_and_url in result:
                    time.sleep(5)
                    filename = name_and_id_and_url[0].replace('[','').replace(']','')  #get the name from the first item in tuple
                    if('https:' in filename):
                        print('attachment is not a file')
                        continue
                    else:
                        saveToDirectory = path+'\\'+ filename
                        url = name_and_id_and_url[2] #get the url from the third item in tuple
                        r = requests.get(url, allow_redirects=True)
                        open(saveToDirectory, 'wb').write(r.content)
            except OSError:
                print ("unable to download file: %s" % saveToDirectory)
            else:
                print ("Successfully downloaded all files to  the directory %s " % path)
                continue

