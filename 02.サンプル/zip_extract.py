import zipfile
with zipfile.ZipFile('13tokyo.zip', 'r') as myzip:
    myzip.extractall()
