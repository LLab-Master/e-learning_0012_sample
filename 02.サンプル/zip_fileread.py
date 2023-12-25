import zipfile
with zipfile.ZipFile('13tokyo.zip', 'r') as myzip:
    with myzip.open('13TOKYO.CSV') as myfile:
        rawtext = myfile.read()
        text=txt = rawtext.decode('shift_jis')
print(text)
