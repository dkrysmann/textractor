import boto3
import os
# Amazon s3
s3 = boto3.resource('s3')
bucket = 'textract-console-eu-west-1-feffc100-d48c-48eb-9c0d-0f1597a47d0d'

content ="Testing for putting text file in s3 bucket"

s3.Object(bucket,'test-file.txt').put(Body=content)

#test_textract_file
# for subdir,dirs,files in os.walk('/test_textract_file'):
# 	for file in fiels:
# 		full_path = os.path.join(subdir,file)
# 		bucket.put_object(Key='/test_textract_file'+full_path[len(path)+1:],Body=content)