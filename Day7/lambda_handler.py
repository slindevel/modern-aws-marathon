import json
import boto3
import requests

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from New Marathon Lambda!')
    }

def lambda_handler_2(event, context):
    bucket_list = ""
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        bucket_list = bucket_list + ', ' + bucket.name
    return {
        'statusCode': 200,
        'body': json.dumps('all buckets: ' + bucket_list)
    }

def lambda_handler_3(event, context):
    r = requests.get('https://www.google.com.tw/')
    return {
        'statusCode': 200,
        'body': json.dumps('all buckets: ' + str(r.status_code))
    }