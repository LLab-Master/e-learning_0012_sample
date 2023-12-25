import json

json_text='''
{
  "氏名":"山田",
  "年齢":33
}
'''

dic = json.loads(json_text)
print(dic['氏名'])
print(dic['年齢'])
