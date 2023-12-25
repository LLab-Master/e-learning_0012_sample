import re
text = '''
<tr>
  <td>1</td>
  <td>PC</td>
  <td>1000</td>
</tr>
'''
pattern = re.compile('<td>(.*)</td>')
result = pattern.findall(text)

for d in result:
    print(d)
