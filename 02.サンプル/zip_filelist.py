import zipfile
with zipfile.ZipFile('13tokyo.zip', 'r') as myzip:    
    for info in myzip.infolist():
        print(info.filename)
