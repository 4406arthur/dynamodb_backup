import boto3
import os
import datetime

def sync_to_s3(target_dir, aws_region, bucket_name):
    if not os.path.isdir(target_dir):
        raise ValueError('target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=aws_region)

    for dirName, subdirList, fileList in os.walk(target_dir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            s3.Object(bucket_name,dirName+'/'+fname+ '_' + datetime.datetime.today().strftime('%Y-%m-%d')).put(Body=open(os.path.join(dirName, fname), 'rb'))

target_dir = 'dump/'
aws_region = 'ap-southeast-1'
bucket_name = 'ddb-backup-ashqkybk8'

sync_to_s3(target_dir,aws_region,bucket_name )
