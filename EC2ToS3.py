import boto3
from datetime import datetime, timedelta
import os

def upload_config():
    bucket = 'bucketName'
    yesterday = datetime.now() - timedelta(days = 1)
    yesterday = yesterday.strftime('%d_%m_%Y')
    file_name = os.listdir('/store/backup/')
    obj_name = yesterday

    s3 = boto3.resource('s3')
    for i in file_name:
        if yesterday in i:
            s3.Bucket(bucket).upload_file('/store/backup/' + i, i)
        
if __name__ == '__main__':
    upload_config()

