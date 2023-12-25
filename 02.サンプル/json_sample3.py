import json
json_text='''
{
"商品リスト": [ 
    {
    "商品名" : "カメラ",
    "値段" : 400
    },
    {
    "商品名" : "PC",
    "値段" : 500
    }
 ]
}
'''
dic = json.loads(json_text)
for item in dic['商品リスト']:
    print(item['商品名'],item['値段'])
