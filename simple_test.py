import boto3
import json


file = '/home/dkrysmann/Pictures/2nd-payment-schiphol.jpg'

with open(file, "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    # print(data)

textract_client = boto3.client('textract', region_name = 'eu-west-1')

# response = textract_client.analyze_document(Document={'Bytes': data},
#         FeatureTypes=["TABLES", "FORMS"])

response = textract_client.detect_document_text(
    Document={'Bytes': data}
)

with open('api_response.json', 'w') as fp:
    json.dump(response, fp)
