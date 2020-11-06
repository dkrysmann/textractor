import json

with open('api_response.json', 'r') as fp:
    data = json.load(fp)
    
for i in data['Blocks']:
    try:
        print({i['Text']})
    except:
        pass
    
'''DocumentMetadata
Blocks
DetectDocumentTextModelVersion
ResponseMetadata'''