import json

json_text='''
{
     "プロフィール": {
        "氏名" : "山田",
        "年齢" : 33
    }
}
'''

dic = json.loads(json_text)
print(dic['プロフィール']['氏名'])
print(dic['プロフィール']['年齢'])
